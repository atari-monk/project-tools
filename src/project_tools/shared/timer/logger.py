"""Logging setup for the timer."""

import logging
from pathlib import Path

from project_tools.const import WORKSPACE_PATH


LOGGER_NAME = "project_tools.timer"
LOG_FILE_NAME = "timer.log"


def get_log_path() -> Path:
    """Return the timer log file path."""
    return Path(WORKSPACE_PATH) / "log" / LOG_FILE_NAME


def configure_logger() -> logging.Logger:
    """Configure console and file logging for the timer."""
    logger = logging.getLogger(LOGGER_NAME)

    if logger.handlers:
        return logger

    log_path = get_log_path()
    log_path.parent.mkdir(parents=True, exist_ok=True)

    logger.setLevel(logging.INFO)
    logger.propagate = False

    formatter = logging.Formatter("%(message)s")

    file_handler = logging.FileHandler(log_path)
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger