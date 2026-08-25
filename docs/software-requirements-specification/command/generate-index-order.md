## Generate order file for documentation index

### Order file

* Generate file `docs/order.txt`.
* The file contains one relative path per line.
* Paths must use `/` as the separator on all platforms.
* If `docs/order.txt` already exists:
  * Preserve existing entries whose files still exist.
  * Append newly discovered files that are missing from the file.
  * Do not add duplicate entries.
  * Remove entries for files that no longer exist.
* If `docs/order.txt` does not exist, create it from all discovered documentation files.
* The order of entries in `order.txt` is the source of truth for the generated documentation index.
* Recursively discover all `.md` files under `docs/`.
* Exclude:
  * `docs/index.md`
  * Any file or directory whose name starts with _.
  * Files in hidden directories/files are not included.
* The command must produce deterministic output.
* Running the command multiple times without filesystem changes must produce no changes.

### Commit

* feat: generate order file for docs index