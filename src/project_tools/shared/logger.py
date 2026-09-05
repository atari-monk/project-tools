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


def setup_custom_logger(
    log_folder_path: Path,
    log_name: str,
    custom_log_name: str
) -> logging.Logger:
    """Return the application logger or an independent custom logger.

    The project-tools log uses the application-wide logger so that it
    writes to the application's configured log file.

    Other custom logs use an independent logger which writes both to the
    console and to its own log file.
    """
    if log_name == "project-tools":
        return logging.getLogger()

    logger = logging.getLogger(f"project-tools.{custom_log_name}.{log_name}")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    log_folder_path.mkdir(parents=True, exist_ok=True)

    has_stream_handler = any(
        isinstance(handler, logging.StreamHandler)
        and not isinstance(handler, logging.FileHandler)
        for handler in logger.handlers
    )

    if not has_stream_handler:
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(logging.Formatter(LOG_FORMAT))
        logger.addHandler(stream_handler)

    add_file_handler(
        logger,
        log_folder_path / f"{log_name}.log",
    )

    return logger 