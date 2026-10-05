## Print docs

- feat: print docs
- command: `proj docs print -p path_to_docs`
- path_to_docs - is any path to docs or folder with md files
- prints categories in docs or folder with md
- implement helpers in module `/home/atari-monk/atari-monk/project/project-tools/src/project_tools/modules/docs`

### Scan docs

- root path has md docs organized in categories folders
- use best data model to represent this file system data
- helper function `scan_docs(path: Path)->data`

### Print docs

- `print_docs(data: ?)->str`
- takes data and renders it to string for console printout
