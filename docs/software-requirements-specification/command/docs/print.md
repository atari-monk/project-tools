## Print docs

### Categories Command

* `proj docs print -p path_to_docs`
* path_to_docs - is any path to docs or folder with md files

#### Behaviour

* Prints categories in docs or folder with md

#### Helpers implementation

Module `/home/atari-monk/atari-monk/project/project-tools/src/project_tools/modules/docs`

#### scan_docs

* Use best data model u want to represent folders data
* Helper function `scan_docs(path: Path)->data`
* Gathers info on folders and stores them in data model
* These folders are in docs or any folder containing md files
* These folders define categories of md files 

#### print_docs

* `print_docs(data: ?)->str`
* Takes data and renders it to string for console printout

### Commits 

* feat: print docs