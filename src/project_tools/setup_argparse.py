import argparse

from project_tools.const import DEL_LOG_CMD
from project_tools import del_log_cmd


COMMANDS = {
    DEL_LOG_CMD: del_log_cmd.run,
}


def setup_argparse() -> None:
    parser = argparse.ArgumentParser( 
        prog="project-tools",
        description="Project maintenance tools.")

    subparsers = parser.add_subparsers(dest="command", metavar="COMMAND",)

    subparsers.add_parser(DEL_LOG_CMD, help="Move the project-tools log file to the trash.")
    
    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        parser.exit()

    COMMANDS[args.command]()
