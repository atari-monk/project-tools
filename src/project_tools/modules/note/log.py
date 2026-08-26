import logging
from pathlib import Path

from project_tools.shared.logger import add_file_handler


logger = logging.getLogger(__name__)


def log_note(
    log_folder: Path,
    log_name: str,
    text: str,
) -> None:
    log_path = log_folder / f"{log_name}.log"


    if log_name != "project-tools":
        add_file_handler(logger, log_path)

    logger.info(text)