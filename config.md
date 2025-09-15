A great example is the [config.json](config.json).

### Config Root

#### `name`

- Default: `"<unknown>"`
- String: name displayed in log.

#### `only_in_release`

- Default: `false`
- False: build normally.
- True: only build with command arg `--release`

#### `src_dir`

- Default: `src/`.
- String: path of source directory.

#### `out_dir`

- Default: `out/`.
- String: path of output directory.

#### `log_level`

- Default: `INFO`.
- String: log level in "DEBUG", "INFO", "WARN", "ERROR", "CRITICAL"
- Integer: log level in 10, 20, 30, 40, 50

#### `compression`

- Default: `STORED`.
- Integer: compression type in 0 (STORED), 8 (DEFLATED), 12 (BZIP2), 14 (LZMA)

#### `compresslevel`

- Default: default for the given compression type.
- Integer:
  - When using `STORED` or `LZMA` this keyword has no effect
  - When using `DEFLATED` integers 0 through 9 are accepted.
  - When using `BZIP2` integers 1 through 9 are accepted.

#### `extra_out_dirs`

- Default: do nothing.
- List of String: paths that copy the output zip to.

#### `exclude_ext`

- Default: Exclude file ends with `[".py", ".backup", ".temp"]`.
- List of String: Exclude files ends with. Dot "." is required, like default value shows.

#### `default_excludes`

- String: exclude a path.
- Dict: [Exclude Tree](#exclude-tree)
- List: exclude trees.

#### `default_merge`

- String: the file starts with this string and will be merged.
- Dict: Merge Tree (same structure as Exclude Tree but merging)
- List: merge trees.

#### `tree`

- Dict: a [Config Tree](#config-tree).
- List: list of config trees.

### Config Tree

#### `inputs`

- String: a path relates to `src_dir`.
- Dict: a [Input Tree](#input-tree)
- List: some inputs.

#### `output`

- Default: do not output loaded data.
- String: a relative path to `out_dir`.

#### `children`

Copy current loaded data to next config tree.

- Dict: config tree.
- List: list of config trees.

### Input Tree

#### `path`

- String: a path relates to `src_dir`. If no `extras`, start reading this path. If has `extras`, this path will used as new relative path.

#### `blocking_mode`

- Default: False.
- False: if file does match `includes` path, load it.
- True: if file does not match `includes` path, block it.

#### `includes`

- String: include a path.
- Dict: [Include Tree](#include-tree)
- List: include trees.

#### `excludes`

- String: exclude a path.
- Dict: [Exclude Tree](#exclude-tree)
- List: exclude trees.

#### `extras`

- String: a path relates to `src_dir`.
- Dict: a [Input Tree](#input-tree)
- List: some inputs.

### Include Tree

#### `path`

- String: a path relates to latest `path`. If no `extras`, include this path. If has `extras`, this path will used as new relative path.

#### `out_path`

- String: a output path relates to latest `out_path`. If no `extras`, moving this path. If has `extras`, this path will used as new relative path.

#### `extras`

- String: a path relates to latest input `path`.
- Dict: a [Include Tree](#include-tree)
- List: some includes.

### Exclude Tree

#### `path`

- String: a path relates to latest `path`. If no `extras`, exclude this path. If has `extras`, this path will used as new relative path.

#### `extras`

- String: a path relates to latest input `path`.
- Dict: a [Exclude Tree](#exclude-tree)
- List: some excludes.
