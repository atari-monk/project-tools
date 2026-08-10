import argparse
from dataclasses import dataclass
from typing import Callable

from project_tools.const import DEL_LOG_CMD, DEL_PROJ_CMD, INIT_CLI_CMD
from project_tools.command import delete_log, delete_proj, init_cli


@dataclass(frozen=True)
class ArgsModel:
    short_flag: str
    flag: str
    required: bool
    help: str


ARGS = {
    INIT_CLI_CMD: [ArgsModel(short_flag = "-p", flag = "--project", required = True, help = "Project name"),
                   ArgsModel(short_flag = "-d", flag = "--description", required = True, help = "Project description"),
                   ArgsModel(short_flag = "-n", flag = "--cli_name", required = True, help = "CLI name"),
                   ArgsModel(short_flag = "-t", flag = "--page_title", required = True, help = "Page title")],
    DEL_PROJ_CMD: [ArgsModel(short_flag = "-p", flag = "--project", required = True, help = "Project name")]
}


def setup_argparse() -> None:
    parser = argparse.ArgumentParser( 
        prog="project-tools",
        description="Project maintenance tools.")

    subparsers = parser.add_subparsers(dest="command", metavar="COMMAND",)

    del_log_parser = subparsers.add_parser(DEL_LOG_CMD, help="Move the project-tools log file to the trash.")
    del_log_parser.set_defaults(func=delete_log.run)

    init_cli_parser = subparsers.add_parser(INIT_CLI_CMD, help="Setup new py cli project.")
    create_command_args(init_cli_parser, INIT_CLI_CMD, init_cli.run)

    del_proj_parser = subparsers.add_parser(DEL_PROJ_CMD, help="Move the project to the trash.")
    create_command_args(del_proj_parser, DEL_PROJ_CMD, delete_proj.run)
    
    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        parser.exit()

    args.func(args)


def create_command_arg(parser: argparse.ArgumentParser, model: ArgsModel):
    parser.add_argument(
        model.short_flag,
        model.flag,
        required = model.required,
        help = model.help,
    )


def create_command_args(
    parser: argparse.ArgumentParser,
    command: str,
    func: Callable[[argparse.Namespace], None],
) -> None:
    parser.set_defaults(func=func)

    for arg in ARGS[command]:
        create_command_arg(parser, arg)
