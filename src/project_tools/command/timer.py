import logging
from argparse import Namespace

from project_tools.const import WORKSPACE_PATH
from project_tools.logger import add_file_handler
from project_tools.shared.timer.duration import (
    InvalidDurationError,
    parse_duration,
)
from project_tools.shared.timer.log import (
    edit_log,
    get_log_path,
    print_log,
)
from project_tools.shared.timer.runner import start_timer


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

    if duration is None:
        args.parser.print_help()
        return

    try:
        seconds = parse_duration(duration)
    except InvalidDurationError as exc:
        logger.error("%s", exc)
        return

    add_file_handler(
        logger,
        WORKSPACE_PATH / "log" / "timer.log",
    )

    logger.info("Starting timer -t %s", duration)

    start_timer(seconds, duration)