use anyhow::{Result, anyhow};
use dashmap::DashMap;
use log::LevelFilter;
use rayon::prelude::*;
use serde_json::Value;
use std::collections::HashMap;
use std::fs::File;
use std::io::BufReader;
use std::path::{Path, PathBuf};
use std::str::FromStr;
pub static mut RELEASE: bool = false;
#[derive(Debug, Clone)]
pub struct Config {
  pub name: String,
  pub src_dir: PathBuf,
  pub out_dir: PathBuf,
  pub extra_out_dirs: Vec<PathBuf>,
  pub excludes: Vec<PathBuf>,
  pub merge: Vec<PathBuf>,
  pub log_level: LevelFilter,
  pub merge_readme: bool,
  pub clear: bool,
}
impl TryFrom<&Value> for Config {
  type Error = anyhow::Error;
  fn try_from(value: &Value) -> std::result::Result<Self, Self::Error> {
    let Value::Object(value) = value else {
      return Err(anyhow!("not a object"));
    };
    if value.get("only_in_release").is_none() && !unsafe { RELEASE } {
      return Err(anyhow!("not in release"));
    }
    Ok(Config {
      name: value.get("name").and_then(|v| v.as_str()).unwrap_or("<unknown>").into(),
      src_dir: value.get("src_dir").and_then(|v| v.as_str()).unwrap_or("src").into(),
      out_dir: value.get("out_dir").and_then(|v| v.as_str()).unwrap_or("out").into(),
      extra_out_dirs: value
        .get("extra_out_dirs")
        .and_then(|v| v.as_array())
        .unwrap_or(&Vec::new())
        .iter()
        .filter_map(|v| v.as_str())
        .map(PathBuf::from)
        .collect(),
      excludes: get_paths(value.get("excludes").unwrap_or(&Value::Null), Path::new(".")),
      merge: todo!(),
      log_level: value
        .get("log_level")
        .and_then(|v| v.as_str())
        .and_then(|s| LevelFilter::from_str(s).ok())
        .unwrap_or(LevelFilter::Info),
      merge_readme: todo!(),
      clear: value.get("clear").and_then(|v| v.as_bool()).unwrap_or(true),
    })
  }
}
impl Config {}
#[macro_export]
macro_rules! debug {
    ($config: expr, $($arg:tt)+) => {
        log::debug!(target: &$config.name, $($arg)+);
    };
}
#[macro_export]
macro_rules! info {
    ($config: expr, $($arg:tt)+) => {
        log::info!(target: &$config.name, $($arg)+);
    };
}
#[macro_export]
macro_rules! warn {
    ($config: expr, $($arg:tt)+) => {
        log::warn!(target: &$config.name, $($arg)+);
    };
}
#[macro_export]
macro_rules! error {
    ($config: expr, $($arg:tt)+) => {
        log::error!(target: &$config.name, $($arg)+);
    };
}
#[derive(Debug, Clone)]
pub struct InputInfo {
  pub path: PathBuf,
  pub blocking_mode: bool,
  pub zip_mode: bool,
  pub excludes: Vec<PathBuf>,
  pub includes: HashMap<PathBuf, Option<PathBuf>>,
}
pub fn is_empty(p: &Path) -> bool { p == Path::new("") || p == Path::new(".") }
pub fn load_json_inputs(path: &Path) -> Result<Value> {
  let file = File::open(path)?;
  let reader = BufReader::new(file);
  Ok(serde_json::from_reader(reader)?)
}
pub fn get_paths_inner(value: &Value, path: &Path, paths: &mut Vec<PathBuf>) {
  match value {
    Value::String(s) => paths.push(path.join(s)),
    Value::Array(arr) => arr.iter().for_each(|item| get_paths_inner(item, path, paths)),
    Value::Object(obj) => {
      let new_path = if let Some(Value::String(path_val)) = obj.get("path") {
        path.join(path_val)
      } else {
        path.to_path_buf()
      };
      if obj.get("type") == Some(&Value::String("load_json".to_string()))
        && let Ok(json_obj) = load_json_inputs(&new_path)
      {
        let parent_path = new_path.parent().unwrap_or(Path::new("."));
        get_paths_inner(&json_obj, parent_path, paths);
        return;
      }
      if let Some(extras) = obj.get("extras") {
        get_paths_inner(extras, &new_path, paths);
      } else {
        paths.push(new_path);
      }
    }
    _ => {}
  }
}
pub fn get_paths(value: &Value, base_path: &Path) -> Vec<PathBuf> {
  let mut r = Vec::new();
  get_paths_inner(value, base_path, &mut r);
  r
}
pub fn get_paths_with_out_inner(
  value: &Value, path_i: &Path, path_o: &Path, paths: &mut HashMap<PathBuf, Option<PathBuf>>,
) {
  match value {
    Value::String(s) => _ = paths.insert(path_i.join(s), None),
    Value::Array(arr) => arr.iter().for_each(|item| get_paths_with_out_inner(item, path_i, path_o, paths)),
    Value::Object(obj) => {
      let new_path_i = if let Some(Value::String(path_val)) = obj.get("path") {
        path_i.join(path_val)
      } else {
        path_i.to_path_buf()
      };
      let new_path_o = if let Some(Value::String(path_val)) = obj.get("out_path") {
        path_o.join(path_val)
      } else {
        path_o.to_path_buf()
      };
      if obj.get("type") == Some(&Value::String("load_json".to_string()))
        && let Ok(json_obj) = load_json_inputs(&new_path_i)
      {
        get_paths_with_out_inner(&json_obj, new_path_i.parent().unwrap_or(Path::new(".")), path_o, paths);
        return;
      }
      if let Some(extras) = obj.get("extras") {
        get_paths_with_out_inner(extras, &new_path_i, &new_path_o, paths);
      } else {
        paths.insert(new_path_i, if is_empty(&new_path_o) { None } else { Some(new_path_o) });
      }
    }
    _ => {}
  }
}
pub fn get_paths_with_out(value: &Value, base: &Path, base_out: &Path) -> HashMap<PathBuf, Option<PathBuf>> {
  let mut r = HashMap::new();
  get_paths_with_out_inner(value, base, base_out, &mut r);
  r
}
pub fn get_inputs_inner(value: &Value, base_info: &InputInfo, inputs: &mut Vec<InputInfo>) {
  match value {
    Value::Array(arr) => arr.iter().for_each(|item| get_inputs_inner(item, base_info, inputs)),
    Value::String(s) => _ = inputs.push(InputInfo { path: base_info.path.join(s), ..base_info.clone() }),
    Value::Object(obj) => {
      let mut _i = base_info.clone();
      if let Some(Value::String(path_str)) = obj.get("path") {
        _i.path = {
          let base: &Path = &base_info.path;
          base.join(path_str)
        };
      };
      if let Some(Value::Bool(zip_mode)) = obj.get("zip_mode") {
        _i.zip_mode = *zip_mode;
      };
      if let Some(Value::Bool(blocking_mode)) = obj.get("mode") {
        _i.blocking_mode = *blocking_mode;
      };
      if let Some(excludes_val) = obj.get("excludes") {
        _i.excludes.extend(get_paths(excludes_val, Path::new(".")));
      };
      if let Some(includes_val) = obj.get("includes") {
        _i.includes.extend(get_paths_with_out(includes_val, Path::new("."), Path::new(".")));
      };
      if obj.get("type") == Some(&Value::String("load_json".to_string()))
        && let Ok(json_obj) = load_json_inputs(&_i.path)
      {
        _i.path = _i.path.parent().unwrap_or(Path::new(".")).into();
        get_inputs_inner(&json_obj, &_i, inputs);
        return;
      }
      if let Some(extras) = obj.get("extras") {
        get_inputs_inner(extras, &_i, inputs);
      } else {
        inputs.push(_i);
      }
    }
    _ => {}
  }
}
pub fn get_inputs(value: &Value, config: &Config) -> Vec<InputInfo> {
  let mut r = Vec::new();
  get_inputs_inner(
    value,
    &InputInfo {
      path: config.src_dir.clone(),
      blocking_mode: false,
      zip_mode: true,
      excludes: Vec::new(),
      includes: HashMap::new(),
    },
    &mut r,
  );
  r
}
pub fn glob(pat: &str, target: &str) -> bool {
  glob::Pattern::new(pat).map(|p| p.matches(target)).unwrap_or(false)
}
pub fn glob_p(pat: &str, target: &Path) -> bool {
  glob::Pattern::new(pat).map(|p| p.matches_path(target)).unwrap_or(false)
}
pub fn globs<T: AsRef<Path> + Sync>(iterable: &[T], target: &str) -> bool {
  iterable.par_iter().any(|pat| {
    let Some(pat_s) = pat.as_ref().to_str() else {
      return false;
    };
    glob(pat_s, target)
  })
}
pub fn globs_p<T: AsRef<Path> + Sync>(iterable: &[T], target: &Path) -> bool {
  iterable.par_iter().any(|pat| {
    let Some(pat_s) = pat.as_ref().to_str() else {
      return false;
    };
    glob_p(pat_s, target)
  })
}
