import logging
from pathlib import Path


def setup_logger(log_folder_path: Path, log_file_name: str) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(log_folder_path / f"{log_file_name}.log"),
        ],
    )