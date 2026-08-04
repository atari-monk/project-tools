## File System Helpers

Create file `file-system.py`

### Dataclass

* Add dataclass `FileSystemResult` with path and created flag

### Create folder 

* Add function `create_folder(parent_path: Path, folder_name: str) -> FileSystemResult`
* Combine folder path
* Check if folder path is dir, return path and false (that means its already there)
* Create folder with parents
* Return path and true

### Create file

* Do it with same workflow but for `create_file(parent_path: Path, file_name: str) -> FileSystemResult`

### Log

* Create a function `log_file_system_result(result: FileSystemResult, logger: Logger) -> None`
* Log created path and aready exists based on result

---

Commit: `feat: file system helpers`
