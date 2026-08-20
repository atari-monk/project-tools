"""Timer log events."""

from datetime import datetime
from logging import Logger


TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M"


def current_timestamp() -> str:
    """Return the current local timestamp in the timer log format."""
    return datetime.now().strftime(TIMESTAMP_FORMAT)


def log_start(logger: Logger) -> None:
    """Log the timer start event."""
    logger.info("start %s", current_timestamp())


def log_stop(logger: Logger) -> None:
    """Log the timer stop event."""
    logger.info("stop %s", current_timestamp())