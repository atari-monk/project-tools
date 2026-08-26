from dataclasses import dataclass
from pathlib import Path
from logging import Logger

@dataclass
class FileSystemResult:
    path: Path
    created: bool


def create_folder(parent_path: Path, folder_name: str) -> FileSystemResult:
    path = parent_path / folder_name

    if path.is_dir():
        return FileSystemResult(path=path, created=False)

    path.mkdir(parents=True)
    return FileSystemResult(path=path, created=True)


def create_file(
    parent_path: Path,
    file_name: str,
    content: str = ""
) -> FileSystemResult:
    path = parent_path / file_name

    if path.is_file():
        return FileSystemResult(path=path, created=False)

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

    return FileSystemResult(path=path, created=True)


def log_file_system_result(result: FileSystemResult, logger: Logger) -> None:
    if result.created:
        logger.info(f"Created: {result.path}")
    else:
        logger.info(f"Already exists: {result.path}")


def create_folder_with_logging(parent_path: Path, folder_name: str, logger: Logger) -> None:
    result =  create_folder(parent_path, folder_name)
    log_file_system_result(result, logger)


def create_file_with_logging(parent_path: Path, file_name: str, content:str, logger: Logger) -> None:
    result =  create_file(parent_path, file_name, content)
    log_file_system_result(result, logger)