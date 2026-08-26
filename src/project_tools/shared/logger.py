import logging
from pathlib import Path


LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"


def setup_logger(
    log_folder_path: Path,
    log_file_name: str,
) -> None:
    """Configure the application-wide logger."""
    logging.basicConfig(
        level=logging.INFO,
        format=LOG_FORMAT,
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(
                log_folder_path / f"{log_file_name}.log"
            ),
        ],
    )


def add_file_handler(
    logger: logging.Logger,
    log_path: Path,
) -> None:
    """Add a file handler to a logger if it is not already present."""
    log_path.parent.mkdir(parents=True, exist_ok=True)

    resolved_path = log_path.resolve()

    for handler in logger.handlers:
        if (
            isinstance(handler, logging.FileHandler)
            and Path(handler.baseFilename).resolve() == resolved_path
        ):
            return

    handler = logging.FileHandler(log_path)
    handler.setFormatter(logging.Formatter(LOG_FORMAT))
    logger.addHandler(handler)