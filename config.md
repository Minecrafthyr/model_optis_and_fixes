A great example is the [config.json](config.json).

### Config Root

Config Tree can hold multiple nested Config Root:

---

Array: [[Config Root](#config-root)]

Object: {

- `name`:
  - Default: `"<unknown>"`
  - String: name displayed in log.
- `only_in_release`: if true, only build with command arg `--release`.
- `src_dir`
  - Default: `src/`.
  - String: path of source directory.
- `out_dir`
  - Default: `out/`.
  - String: path of output directory.
- `log_level`
  - String: log level in "DEBUG", "INFO" (default), "WARN", "ERROR", "CRITICAL"
  - Integer: log level in 10, 20, 30, 40, 50
- `compression`: Integer compression type in 0 (STORED) (default), 8 (DEFLATED), 12 (BZIP2), 14 (LZMA). Always DEFLATED if `--release`.
- `compresslevel`:
  - Default: default for the given compression type.
  - Integer: `DEFLATED` accept 0 to 9, `BZIP2` accept 1 to 9. Always 9 if `--release`.
- `extra_out_dirs`: List of string paths that copy the output zip to.
- `exclude_ext`:
  - Default: Exclude file ends with `(".py", ".backup", ".temp")`.
  - List of String: Exclude files ends with. Dot "." is required, like default value shows.
- `default_excludes`: [Path Tree](#path-tree) that default excludes.
- `default_merge`: [Path Tree](#path-tree) that default merging.
- `tree`: [Config Tree](#config-tree).

}

### Config Tree

Config Tree controls I/O and can hold multiple nested Config Tree:

---

Array: [[Config Tree](#config-tree)]

Object: {

- `removes`: [Path Tree](#path-tree) that remove stored data in copied storage.
- `inputs`\*: [Input Tree](#input-tree) that put files into storage.
- `output`: String that output stored data to a zip file at `{out_dir}/{output}.zip`
- `children`: Config Tree that copy current stored data and entering.

}

### Path Tree

Path Tree will transmute structure into set of strings. The result could be directory or file:

---

Array: [[Path Tree](#path-tree)]

String: a path relates to latest path.

Object: {

- `path`: a path relates to latest path. If no `extras`, add this path into result. If has `extras`, this path will used as a new relative path.
- `extras`: a Path Tree.

}

### Input Tree

Path Tree will transmute structure into set of strings. The result could be directory or file:

---

Array: [[Input Tree](#input-tree)]

String: a path relates to latest path. If it ends with `input_config.json`, it could read that file as a nested input tree.

Object: {

- `path`: a path relates to latest path. If no `extras`, add this path into result. If has `extras`, this path will used as a new relative path.
- `blocking_mode`:
  - False (default): if file does match `includes` path, load it.
  - True: if file does not match `includes` path, block it.
- `includes`: [Path Tree with Output](#path-tree-with-output) to include.
- `excludes`: [Path Tree](#path-tree) to exclude.
- `extras`: a [Input Tree](#input-tree)

}

### Path Tree with Output

Path Tree with Output will transmute structure into tuples of (string, string). The result could be (directory, new directory or none) or (file, new file or none):

- Array: [[Path Tree](#path-tree)]
- String: a path relates to latest path.
- Object: {

  - `path`: a path relates to latest path. If no `extras`, add this path into result. If has `extras`, this path will used as a new relative path.
  - `out_path`: a output path relates to latest out path. If no `extras`, add this out path into result. If has `extras`, this path will used as new relative out path.
  - `extras`: a Path Tree.

  }
