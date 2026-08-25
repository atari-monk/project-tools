from argparse import Namespace
from typing import cast

from project_tools.const import NOTE_LOG_CONFIG_PATH, WORKSPACE_PATH
from project_tools.shared.note import load_config, log_note


def run(args: Namespace) -> None:
    if args.print:
        config = load_config(NOTE_LOG_CONFIG_PATH)

        for log_name in config.logs:
            print(log_name)

        return

    if args.log is None or args.text is None:
        args.parser.error(
            "the following arguments are required: -l/--log and -t/--text"
        )

    log_name = cast(str, args.log)
    text = cast(str, args.text)

    config = load_config(NOTE_LOG_CONFIG_PATH)

    if not config.contains(log_name):
        args.parser.error(
            f"invalid log '{log_name}'. "
            f"choose from: {', '.join(config.logs)}"
        )

    log_note(
        WORKSPACE_PATH / "log",
        log_name,
        text,
    )