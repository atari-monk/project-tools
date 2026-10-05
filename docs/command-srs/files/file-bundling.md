## File Bundling

### Argparse setup

- feat: file bundler
- command: `proj bundle -o path -p paths`
- add --out alias
- o is a path to output file
- add --paths alias
- p can have many paths

### Data

- define list of ignored folders
- define list of ignored files
- define list of extensions that are supported files
- define table of languages used in md in pairs `file extension: language`
- add py model
- add data file in simplest format in path `/home/atari-monk/atari-monk/project/project-tools/data/bundle.json`

### Helper Functions

- use folder `src/project_tools/modules/bundle`
- add function loading model with config data defined above
- add function `bundle_files(out: Path, paths:[]Path)`:
  - take config into account
  - if path is a folder, take all supported files in path recursivly and render them to markdown file
  - if path is a file add it to md
  - do paths in order of args provided by cli command
  - store md in out path from args
  - use format:

````md
## file path

```language
file content
```
````

- if language is md, use ```` markers
