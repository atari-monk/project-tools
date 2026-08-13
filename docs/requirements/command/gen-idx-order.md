# Requirements - Generate Documentation Index Order Command

### [Add Command boilerplate](../../how-to/project-tools/add-command.md)

## Order file

* Generate file `docs/order.txt`.
* The file contains one relative path per line.
* Paths must use `/` as the separator on all platforms.
* If `docs/order.txt` already exists:

  * Preserve existing entries whose files still exist.
  * Append newly discovered files that are missing from the file.
  * Do not add duplicate entries.
  * Ignore entries for files that no longer exist.
* If `docs/order.txt` does not exist, create it from all discovered documentation files.
* The order of entries in `order.txt` is the source of truth for the generated documentation index.
* Blank lines should not be generated.
* `docs/order.txt` and `docs/index.md` must never be included in the order.

## Indexed files

* Recursively discover all `.md` files under `docs/`.
* Exclude:

  * `docs/index.md`
  * Any file or directory whose name starts with _.
  * Files in hidden directories/files are not included.
* The command must produce deterministic output.
* Running the command multiple times without filesystem changes must produce no changes.

## Processing rules

1. Discover all eligible `.md` files under `docs/`.
2. Exclude `index.md`.
3. Read the existing `order.txt`, if present.
4. Preserve existing entries whose files still exist.
5. Append newly discovered files that are missing from `order.txt` in deterministic filesystem-independent order.
6. Remove entries whose files no longer exist.
7. Write the resulting paths to `docs/order.txt`.
8. Write paths using `/` separators.
9. Generate `docs/index.md` using the resulting `order.txt` order.
10. The command must be idempotent.

## Error handling

* If `docs/` does not exist, create it before generating the order.
* If a file listed in `order.txt` no longer exists, silently remove it from the generated `order.txt`.
* Invalid or malformed paths in `order.txt` should not cause files outside `docs/` to be indexed.
* The command should fail with a non-zero exit code when the order file or index file cannot be read or written.

## Acceptance criteria

* A missing `docs/order.txt` is created.
* A missing `docs/index.md` is created.
* Existing `order.txt` ordering is preserved.
* New documentation files are appended to `order.txt`.
* Deleted documentation files are removed from `order.txt`.
* `index.md` follows the exact ordering from `order.txt`.
* Documentation is grouped into folder-based sections.
* Root-level documentation is placed under `### Root`.
* Kebab-case names are converted to human-readable title case.
* Generated paths are relative to `docs/`.
* `index.md` and `order.txt` are never indexed.
* Files and directories whose names start with _ are never indexed.
* Running the command twice without filesystem changes produces identical output.

Commit: `feat: generate docs index order command`
