"""Background timer worker."""

import argparse
import time

from project_tools.shared.timer.events import log_start, log_stop
from project_tools.shared.timer.logger import configure_logger
from project_tools.shared.timer.notification import notify_timer_finished
from project_tools.shared.timer.sound import play_timer_finished_sound


def run(seconds: float) -> None:
    """Run a timer in the background process."""
    logger = configure_logger()

    log_start(logger)

    try:
        time.sleep(seconds)
    finally:
        log_stop(logger)
        notify_timer_finished()
        play_timer_finished_sound()


def create_parser() -> argparse.ArgumentParser:
    """Create the worker argument parser."""
    parser = argparse.ArgumentParser(description="Project-tools timer worker.")
    parser.add_argument("seconds", type=float)

    return parser


def main() -> None:
    """Run the timer worker CLI."""
    parser = create_parser()
    args = parser.parse_args()

    run(args.seconds)


if __name__ == "__main__":
    main()