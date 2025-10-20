A great example is the [config.json](config.json).

> [!WARN]
> All path matching now uses glob pattern matching (see Python fnmatch/glob syntax).  

### Config Root Tree

A Config File and hold multiple nested Config Root Tree.

---

Array: [[Config Root](#config-root)]

Object: {

- `name`: String that is name displayed in log, or `"<unknown>"`
- `only_in_release`: if true, only build with command arg `--release`.
- `src_dir`: path of source directory (default is `src/`).
- `out_dir`: path of output directory (default is `out/`).
- `log_level`
  - String: log level in "DEBUG", "INFO" (default), "WARN", "ERROR", "CRITICAL"
  - Integer: log level in 10, 20, 30, 40, 50
- `extra_out_dirs`: List of string paths that copy the output zip to.
- `excludes`: [Path Tree](#path-tree) that default excludes with glob.
- `merge`: [Path Tree](#path-tree) that default merging.
- `tree`: [Config Tree](#config-tree) if not present, config will not load, useful for `children`.
- `children`: [Config Root Tree](#config-root-tree).

}

### Config Tree

Config Tree controls I/O and can hold multiple nested Config Tree:

---

Array: [[Config Tree](#config-tree)]

Object: {

- `removes`: [Path Tree](#path-tree) that remove stored data in copied storage start with `removes`.
- `inputs`\*: [Input Tree](#input-tree) that put files into storage.
- `output`: String that output stored data to a zip file at `{out_dir}/{output}.zip`
- `children`: Config Tree that copy current stored data and entering.

}

### Path Tree

Path Tree will transmute structure into a set of glob patterns (strings). The result could be a directory or file:

---

Array: [[Path Tree](#path-tree)]

String: a path relates to latest path.

Object: {

- `type`: if `load_json`, set directory to the dirname of `path`, and read `path` file as [Path Tree](#path-tree).
- `path`: a path relates to latest path, supports glob patterns. If no `extras`, add this path into result. If has `extras`, this path will be used as a new relative path.
- `extras`: a Path Tree.

}

### Path Tree with Output

Path Tree with Output will transmute structure into tuples of (string, string). The result could be (directory, new directory or none) or (file, new file or none):

Array: [[Path Tree with Output](#path-tree-with-output)]

String: a path relates to latest path.

Object: {

  - `type`: if `load_json`, set directory to the dirname of `path`, and read `path` file as [Path Tree with Output](#path-tree-with-output).
  - `path`: a path relates to latest path. If no `extras`, add this path into result. If has `extras`, this path will used as a new relative path.
  - `out_path`: a output path relates to latest out path. If no `extras`, add this out path into result. If has `extras`, this path will used as new relative out path.
  - `extras`: a [Path Tree with Output](#path-tree-with-output).

  }

### Input Tree

Path Tree will transmute structure into set of strings. The result could be directory or file:

---

Array: [[Input Tree](#input-tree)]

String: a path relates to latest path.

Object: {

- `type`: if `load_json`, set directory to the dirname of `path`, and read `path` file as [Input Tree](#input-tree).
- `path`: a path relates to latest path. If no `extras`, add this path into result. If has `extras`, this path will used as a new relative path.
- `blocking_mode`:
  - False (default): if file does match `includes` path, load it.
  - True: if file does not match `includes` path, block it.
- `includes`: [Path Tree with Output](#path-tree-with-output) to include.
- `excludes`: [Path Tree](#path-tree) to exclude.
- `extras`: a [Input Tree](#input-tree)

}
