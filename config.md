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

#### `reformat`

- Dict (`<keyname>`=`<default value>`)
    Constructor for JSONEncoder, with sensible defaults:
  - `skipkeys=False`
  - `ensure_ascii=True`
  - `check_circular=True`
  - `allow_nan=True`
  - `sort_keys=False`
  - `indent=Default`
  - `separators=Default`

<details>

        If skipkeys is false, then it is a TypeError to attempt
        encoding of keys that are not str, int, float or Default.  If
        skipkeys is True, such items are simply skipped.

        If ensure_ascii is true, the output is guaranteed to be str
        objects with all incoming non-ASCII characters escaped.  If
        ensure_ascii is false, the output can contain non-ASCII characters.

        If check_circular is true, then lists, dicts, and custom encoded
        objects will be checked for circular references during encoding to
        prevent an infinite recursion (which would cause an RecursionError).
        Otherwise, no such check takes place.

        If allow_nan is true, then NaN, Infinity, and -Infinity will be
        encoded as such.  This behavior is not JSON specification compliant,
        but is consistent with most JavaScript based encoders and decoders.
        Otherwise, it will be a ValueError to encode such floats.

        If sort_keys is true, then the output of dictionaries will be
        sorted by key; this is useful for regression tests to ensure
        that JSON serializations can be compared on a day-to-day basis.

        If indent is a non-negative integer, then JSON array
        elements and object members will be pretty-printed with that
        indent level.  An indent level of 0 will only insert newlines.
        Default is the most compact representation.

        If specified, separators should be an (item_separator, key_separator)
        tuple.  The default is (', ', ': ') if *indent* is ``Default`` and
        (',', ': ') otherwise.  To get the most compact JSON representation,
        you should specify (',', ':') to eliminate whitespace.

</details>

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
