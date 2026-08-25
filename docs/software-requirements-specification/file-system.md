## File system helpers

Helper functions for file system operations.

### Dataclass

* Create file `file_system.py` 
* Add dataclass `FileSystemResult` with path and created flag

### Create folder 

* Add function `create_folder(parent_path: Path, folder_name: str) -> FileSystemResult`
* Combine folder path
* Check if folder path is dir, return path and false (that means its already there)
* Create folder with parents
* Return path and true

### Create file

* Add function `create_file(parent_path: Path, file_name: str, content:str = "") -> FileSystemResult`
* Use `write_text` with content

### Log

* Create a function `log_file_system_result(result: FileSystemResult, logger: Logger) -> None`
* Log created path and aready exists based on result

### Convenience Functions

* Add function `create_folder_with_logging(parent_path: Path, folder_name: str, logger: Logger) -> None`
* Add function `create_file_with_logging(parent_path: Path, file_name: str, content:str, logger: Logger) -> None`
* Use `create_folder` or `create_file` and `log_file_system_result`

### Commits

* feat: file system helpers