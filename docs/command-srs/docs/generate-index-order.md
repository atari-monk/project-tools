# Order file

Generate docs index order file for a documentation folder

## File

- feat: generate order file for docs index
- generate file `docs/order.txt`
- file contains one relative path per line
- paths must use `/` as the separator on all platforms
- if `docs/order.txt` does not exist, create it from all discovered documentation files
- order of entries in `order.txt` is the source of truth for the generated documentation index

### Discovery

- recursively discover all `.md` files under `docs/`
- exclude:
  - `docs/index.md`
  - any file or directory whose name starts with `_`
  - files in hidden directories or hidden files

- command must produce deterministic output
- running the command multiple times without filesystem changes must produce no changes

### Existing order file

If `docs/order.txt` already exists:

- preserve existing entries whose files still exist
- append newly discovered files that are missing from the file
- do not add duplicate entries
- remove entries for files that no longer exist

### Generic path

- accept a folder path as an argument

### Command definition

```yaml
commands:
  docs:
    help: Documentation commands.

    commands:
      gen_idx_order:
        help: Generate docs index order for project.
        function: generate_index_order.run
        args:
          - short_flag: "-p"
            flag: "--path"
            required: true
            type: path
            help: Path to folder with md docs
```
