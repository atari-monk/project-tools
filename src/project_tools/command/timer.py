from argparse import Namespace
import logging

from project_tools.shared.timer.duration import (
    InvalidDurationError,
    parse_duration,
)
from project_tools.shared.timer.log import edit_log, print_log
from project_tools.shared.timer.logger import get_log_path
from project_tools.shared.timer.runner import start_timer # type: ignore


logger = logging.getLogger(__name__)

POMODORO_DURATION = "25m"


def run(args: Namespace) -> None:
    """Run the timer command."""
    if (
        args.time is None
        and not args.pomodoro
        and not args.print_log
        and not args.edit
    ):
        args.parser.print_help()
        return

    if args.print_log:
        print_log(get_log_path())

    if args.edit:
        edit_log(get_log_path())

    if not args.time and not args.pomodoro:
        return

    duration = POMODORO_DURATION if args.pomodoro else args.time

    try:
        seconds = parse_duration(duration)
    except InvalidDurationError as exc:
        logger.error("%s", exc)
        return

    start_timer(seconds)

    logger.info("Timer started: %s", duration)