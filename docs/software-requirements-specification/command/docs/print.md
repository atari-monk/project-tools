## Print docs

### Categories Command

* `proj docs print -p path_to_docs`
* path_to_docs - is any path to docs or folder with md files

#### Behaviour

* Prints categories in docs or folder with md

#### Helpers implementation

Module `/home/atari-monk/atari-monk/project/project-tools/src/project_tools/modules/docs`

#### scan_docs

* Dataclass `DocsCategories` with file system data
* Helper function `scan_docs(path: Path)->DocsCategories`
* Gathers info on folders and stores them in `DocsCategories` data
* These folders are in docs or md files parent and contain md files
* These folders define categories of md files 

#### print_docs

* `print_docs(DocsCategories)->str`
* Takes `DocsCategories` and renders it to string for console printout

### Commits 

* feat: print docs