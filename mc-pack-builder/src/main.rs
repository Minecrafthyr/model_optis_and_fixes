use anyhow::{Result, anyhow};
use chrono::{DateTime, Local};
use dashmap::DashMap;
use log::LevelFilter;
use rayon::prelude::*;
use serde_json::{Value, from_slice};
use std::ffi::OsStr;
use std::fs::{self, File};
use std::io::{BufWriter, Read, Write, stdin};
use std::path::{Path, PathBuf};
use std::result::Result::Ok;
use std::time::Instant;
use walkdir::WalkDir;
use zip::ZipArchive;
use zip::{ZipWriter, write::SimpleFileOptions};
type Storage = DashMap<PathBuf, Vec<u8>>;
mod args_x;
mod merge;
mod path;
use crate::args_x::ArgsX;
use path::*;
fn is_excluded(path: &Path, config: &Config, excludes: &[PathBuf]) -> bool {
  if globs_p(excludes, path) || globs_p(&config.excludes, path) {
    debug!(config, "excluded \"{}\"", path.display());
    true
  } else {
    false
  }
}
fn moving(path_o: &Path, config: &Config, ii: &InputInfo) -> PathBuf {
  match ii.includes.get(path_o).and_then(|p| p.as_ref().filter(|p| !is_empty(p))) {
    Some(p) => {
      debug!(config, "Moved {} to {}", path_o.display(), p.display());
      p.to_path_buf()
    }
    _ => path_o.to_path_buf(),
  }
}
fn store(storage: &Storage, config: &Config, ii: &InputInfo, mut buf: Vec<u8>, path_o: &Path) -> Result<()> {
  let moved = moving(path_o, config, ii);
  if moved.ends_with(".json")
    && let Some(stored) = storage.get(&moved)
    && globs_p(&config.merge, &moved)
  {
    let mut existing_value: Value = from_slice(stored.value())?;
    let new_value: Value = from_slice(&buf)?;
    if let (Value::Object(existing_obj), Value::Object(new_obj)) = (&mut existing_value, new_value) {
      existing_obj.extend(new_obj);
      buf = serde_json::to_vec(&existing_value)?;
    }
  } else if config.merge_readme
    && let Some(filename) = moved.file_name()
    && filename.eq_ignore_ascii_case("readme.md")
    && let Some(mut existing) = storage.get_mut(&moved)
  {
    if !existing.value().ends_with(b"\n") {
      existing.value_mut().push(b'\n');
    }
    existing.value_mut().extend_from_slice(&buf);
    return Ok(());
  }
  storage.insert(moved, buf);
  Ok(())
}
fn process_input(storage: &Storage, config: &Config, ii: &InputInfo) -> Result<()> {
  let is_dir = ii.path.is_dir();
  let is_file = ii.path.is_file();
  if !is_dir && !is_file {
    return Err(anyhow!("not dir or path"));
  }
  if is_dir {
    debug!(config, "Loading directory {}", ii.path.display());
    WalkDir::new(&ii.path)
      .into_iter()
      .filter_map(|e| e.ok())
      .filter(|e| e.file_type().is_file())
      .collect::<Vec<_>>()
      .par_iter()
      .try_for_each(|entry| {
        let path_i = entry.path();
        let path_o = path_i.strip_prefix(&ii.path).unwrap_or(path_i);
        if is_excluded(path_o, config, &ii.excludes) {
          return Ok(());
        }
        store(storage, config, ii, fs::read(path_i)?, path_o)
      })?;
  }
  if is_file {
    if ii.zip_mode && ii.path.extension().and_then(|ext| ext.to_str()) == Some("zip") {
      debug!(config, "Loading zip file {}", ii.path.display());
      let mut zip = ZipArchive::new(File::open(&ii.path)?)?;
      for i in 0..zip.len() {
        let mut zip_file = zip.by_index(i)?;
        if zip_file.is_dir() {
          continue;
        }
        let Some(mut file_name) = zip_file.enclosed_name() else {
          return Err(anyhow!("invalid zip path"));
        };
        if is_excluded(Path::new(&file_name), config, &ii.excludes) {
          continue;
        }
        let mut content = Vec::new();
        zip_file.read_to_end(&mut content)?;
        if let Some(Some(x)) = ii.includes.get(&file_name) {
          file_name = x.clone();
        }
        storage.insert(file_name, content);
      }
      Ok(())
    } else {
      store(storage, config, ii, fs::read(&ii.path)?, match ii.path.file_name() {
        Some(s) => Path::new(s),
        None => return Err(anyhow!("unknown path")),
      })
    }?;
  }
  Ok(())
}
fn create_zip_output(storage: &Storage, output_path: &Path, config: &Config) -> Result<()> {
  if let Some(parent) = output_path.parent() {
    fs::create_dir_all(parent)?;
  }
  let mut zip = ZipWriter::new(BufWriter::new(File::create(output_path)?));
  let file_opt = SimpleFileOptions::default().compression_level(Some(if unsafe { RELEASE } { 9 } else { 1 }));
  for pair in storage {
    zip.start_file(pair.key().to_string_lossy(), file_opt)?;
    zip.write_all(pair.value())?;
  }
  zip.finish()?;
  let file_size = output_path.metadata()?.len() >> 10;
  info!(config, "\"{}\" completed ({} files, {} KiB)", output_path.display(), storage.len(), file_size);
  Ok(())
}
fn extra_out(path_o: &Path, file_name: &OsStr, config: &Config) {
  let mut success = Vec::new();
  let mut invaild = Vec::new();
  for p in &config.extra_out_dirs {
    if p.is_absolute() && p.exists() {
      let p = p.join(file_name);
      if fs::copy(&path_o, &p).is_ok() { &mut success } else { &mut invaild }.push(p.display().to_string())
    } else {
      invaild.push(p.display().to_string());
    }
  }
  if !success.is_empty() {
    debug!(config, "Copied \"{}\" to \"{:?}\"", path_o.display(), success);
  }
  if !invaild.is_empty() {
    error!(config, "Error copy \"{}\" to \"{:?}\"", path_o.display(), invaild);
  }
}
fn process_tree(tree: &Value, storage: Storage, config: &Config) -> Result<()> {
  let start_time = Instant::now();
  if let Some(removes) = tree.get("removes") {
    for path in get_paths(removes, Path::new(".")) {
      if storage.remove(&path).is_some() {
        debug!(config, "Removed {} from storage", path.display());
      }
    }
  }
  for _ii in get_inputs(
    match tree.get("inputs") {
      Some(s) => s,
      None => return Err(anyhow!("no inputs")),
    },
    config,
  ) {
    process_input(&storage, config, &_ii)?
  }
  if let Some(output) = tree.get("outputs").and_then(|v| v.as_str()) {
    std::thread::scope(|s| -> Result<()> {
      if let Some(children) = tree.get("children") {
        s.spawn(|| process_tree_children(children, &storage, &config));
      };
      let path_o = config.out_dir.join(output.to_owned() + ".zip");
      create_zip_output(&storage, &path_o, config)?;
      if tree.get("extra_out").and_then(|v| v.as_bool()).unwrap_or(true)
        && !config.extra_out_dirs.is_empty()
        && let Some(file_name) = path_o.file_name()
      {
        extra_out(&path_o, file_name, config);
      };
      Ok(())
    })?;
  } else if let Some(children) = tree.get("children") {
    process_tree_children(children, &storage, config)?;
  }
  debug!(config, "{}: Tree processing completed in {:.2}s", config.name, start_time.elapsed().as_secs_f32());
  Ok(())
}
fn process_tree_children(children: &Value, storage: &Storage, config: &Config) -> Result<()> {
  match children {
    Value::Array(arr) =>
      arr.par_iter().try_for_each(|child| process_tree(&child.clone(), storage.clone(), config)),
    Value::Object(_) => process_tree(&children.clone(), storage.clone(), config),
    _ => Ok(()),
  }
}
fn process_config(value: Value) -> Result<()> {
  if let Value::Array(arr) = value {
    arr.into_par_iter().map(process_config).collect::<Result<Vec<()>>>()?;
    return Ok(());
  }
  let config = Config::try_from(&value)?;
  info!(config, "== Config \"{}\" starts ==", config.name);
  if config.clear && config.out_dir.exists() {
    fs::remove_dir_all(&config.out_dir)?;
  }
  fs::create_dir_all(&config.out_dir)?;
  process_tree(&value["tree"], DashMap::new(), &config)?;
  Ok(())
}
fn setup_logger(log_file: &Path) -> Result<()> {
  if log_file.exists()
    && let Some(filename) = log_file.file_name()
    && let Ok(metadata) = log_file.metadata()
    && let Ok(modified) = metadata.modified()
  {
    fs::copy(
      log_file,
      format!("{} {}", DateTime::<Local>::from(modified).format("%F_%H-%M-%S%z"), filename.display()),
    )?;
  }
  fern::Dispatch::new()
    .chain(
      fern::Dispatch::new()
        .level(LevelFilter::Info)
        .format(|out, message, record| {
          out.finish(format_args!("[{}] [{}] {}", Local::now().format("%T"), record.level(), message))
        })
        .chain(std::io::stdout()),
    )
    .chain(
      fern::Dispatch::new()
        .level(LevelFilter::Debug)
        .format(|out, message, record| {
          out.finish(format_args!("[{}] [{}] {}", Local::now().format("%T%.3f"), record.level(), message))
        })
        .chain(fern::log_file(log_file)?),
    )
    .apply()?;
  Ok(())
}
fn main() -> Result<()> {
  let args = ArgsX::new();
  unsafe {
    RELEASE = args.release;
  }
  std::env::set_current_dir(&args.dir)?;
  setup_logger(&args.log)?;
  let start_time = Instant::now();
  let buf = {
    let c = match args.config {
      None => {
        println!("Starts with stdin mode, use Ctrl+Z (Windows) or Ctrl+D (Linux) as input end.");
        let mut buf = Vec::new();
        stdin().read_to_end(&mut buf)?;
        buf
      }
      Some(path_buf) => fs::read(&path_buf)?,
    };
    log::info!("Build starts at {}", Local::now().format("%+"));
    c
  };
  process_config(serde_json::from_slice(&buf)?)?;
  log::info!("Build completed in {:.2}s", start_time.elapsed().as_secs_f32());
  Ok(())
}
