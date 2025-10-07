use std::{path::PathBuf, process::exit};
#[derive(Debug)]
pub struct ArgsX {
  pub dir: PathBuf,
  pub config: Option<PathBuf>,
  pub log: PathBuf,
  pub release: bool,
}
impl Default for ArgsX {
  fn default() -> Self {
    Self {
      dir: PathBuf::from("."),
      config: Default::default(),
      release: Default::default(),
      log: PathBuf::from("build.log"),
    }
  }
}
macro_rules! help {
  ($s:expr) => {
    concat!($s, " Use \"mcpb help\" for help.")
  };
}
macro_rules! param {
  ($args:expr, $s:expr) => {
    $args.next().expect(help!(concat!("Missing param <", $s, ">.")))
  };
}
impl ArgsX {
  pub fn params(&mut self, args: &mut std::env::Args, s: &str) -> bool {
    match s {
      "-d" | "--dir" => self.dir = param!(args, "path").into(),
      "-l" | "--log" => self.log = param!(args, "path").into(),
      "-r" | "--release" => self.release = true,
      _ => panic!(help!("Invalid input args.")),
    }
    true
  }
  pub fn new() -> ArgsX {
    let mut args = std::env::args();
    args.next().expect("no args???");
    let mut args_x = ArgsX::default();
    match args.next().expect(help!("Missing arg.")).as_str() {
      "help" | "-h" | "--help" => {
        print!(include_str!("text/help.txt"));
        exit(-1);
      }
      "about" | "-a" | "--about" => {
        print!(include_str!("text/about.txt"));
        exit(-1);
      }
      "run" => args_x.config = Some(param!(args, "path").into()),
      "input" => args_x.config = None,
      arg =>
        if !args_x.params(&mut args, arg) {
          return args_x;
        },
    };
    while let Some(arg) = args.next()
      && args_x.params(&mut args, &arg)
    {}
    args_x
  }
}
