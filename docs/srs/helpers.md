## Helpers

### File system

Helper functions for file system operations

#### Dataclass

- create file `file_system.py`
- add dataclass `FileSystemResult` with path and created flag

#### Create folder

- add function `create_folder(parent_path: Path, folder_name: str) -> FileSystemResult`
- combine folder path
- check if folder path is dir, return path and false (that means its already there)
- create folder with parents
- return path and true

#### Create file

- add function `create_file(parent_path: Path, file_name: str, content:str = "") -> FileSystemResult`
- use `write_text` with content

#### Log

- create a function `log_file_system_result(result: FileSystemResult, logger: Logger) -> None`
- log created path and aready exists based on result

#### Convenience Functions

- add function `create_folder_with_logging(parent_path: Path, folder_name: str, logger: Logger) -> None`
- add function `create_file_with_logging(parent_path: Path, file_name: str, content:str, logger: Logger) -> None`
- use `create_folder` or `create_file` and `log_file_system_result`
- feat: file system helpers

### Logger

- create file `src/project_tools/logger.py`
- import py logging
- add `setup_logger(log_folder_path: Path, log_file_name: str) -> None`
  - default level info
  - format - timestamp, level, message
  - handle terminal and file log

### Main

Cli app main entrypoint

- create file `src/project_tools/cli.py`
- add `main() -> None`
- use modules to:
  - create foler `WORKSPACE_PATH / "log"`
  - setup logger with `WORKSPACE_PATH / "log" / "project-tools.log"`
  - setup argparse
