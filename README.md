- [Description](Description.md) used in Modrinth and Curseforge.
- [Credit Links](CreditLinks.md)
- [LICENSE](src/Base/LICENSE) and additional license notice [LICENSE.1](src/Base/LICENSE.1)

## Custom Build

1. Clone Github Repository
2. Config `config.json` following [`config.md`](config.md)
3. Install Python 3.14
4. Enter path `cd <the path>`
5. `pip install jsonpatch`
6. `python build.py`
   - `-r`, `--release` arg build config root with tag `only_in_release` is true and do more compressions.
   - `-r`, `--dir` `<path>` arg change the current directory path.
   - `-c`, `--cfg` `<path>` arg change the config path.
   - `-l`, `--log` `<path>` arg change the log path.
