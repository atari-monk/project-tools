"""Background timer worker."""

import argparse
import logging
import time

from project_tools.const import WORKSPACE_PATH
from project_tools.logger import add_file_handler, setup_logger
from project_tools.shared.timer.events import log_stop
from project_tools.shared.timer.notification import notify_timer_finished
from project_tools.shared.timer.sound import play_timer_finished_sound


logger = logging.getLogger(__name__)


def run(seconds: float, duration: str) -> None:
    """Run a timer in the background process."""

    setup_logger(
        WORKSPACE_PATH / "log",
        "project-tools",
    )

    add_file_handler(
        logger,
        WORKSPACE_PATH / "log" / "timer.log",
    )

    try:
        time.sleep(seconds)
    finally:
        log_stop(logger, duration)
        notify_timer_finished()
        play_timer_finished_sound()


def create_parser() -> argparse.ArgumentParser:
    """Create the worker argument parser."""
    parser = argparse.ArgumentParser(
        description="Project-tools timer worker.",
    )
    parser.add_argument("seconds", type=float)
    parser.add_argument("duration")
    return parser


def main() -> None:
    """Run the timer worker CLI."""
    parser = create_parser()
    args = parser.parse_args()

    run(args.seconds, args.duration)


if __name__ == "__main__":
    main()