## File Bundling

### Argparse setup

* Setup command boilerplate for `proj bundle -o path -p paths`
* Add --out alias.
* Where o is a path to output file
* Add --paths alias.
* Where p can have multiple paths

### Data

* Define list of ignored folders
* Define list of ignored files
* Define list of extensions that are supported files
* Define table of languages used in md in pairs `file extension: language` 
* Add py model
* Add data file in simplest format in path `/home/atari-monk/atari-monk/project/project-tools/data/bundle.json`

### Helper Functions

* Use container `src/project_tools/shared/bundle`
* Add function loading model with config data defined above
* Add function `bundle_files(out: Path, paths:[]Path)`:
    * Take config into account
    * If path is a folder, take all supported files in path recursivly and render them to markdown file
    * If path is a file add it to md
    * Do paths in order of args provided by cli command
    * Store md in out path from args
    * Use format:

## file path

```language
file content
```
...

* If language is md, give ```` markers

### Commit

* feat: file bundler