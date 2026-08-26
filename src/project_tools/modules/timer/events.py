import logging


def log_start(logger: logging.Logger, duration: str) -> None:
    """Log the timer start event."""
    logger.info("Starting timer -t %s", duration)


def log_stop(logger: logging.Logger, duration: str) -> None:
    """Log the timer stop event."""
    logger.info("Stopping timer -t %s", duration)