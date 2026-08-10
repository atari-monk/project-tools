import argparse
from dataclasses import dataclass

from project_tools.const import DEL_LOG_CMD, INIT_CLI_CMD
from project_tools.command import delete_log, init_cli


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
                   ArgsModel(short_flag = "-t", flag = "--page_title", required = True, help = "Page title")]
}


def setup_argparse() -> None:
    parser = argparse.ArgumentParser( 
        prog="project-tools",
        description="Project maintenance tools.")

    subparsers = parser.add_subparsers(dest="command", metavar="COMMAND",)

    delete_log_parser = subparsers.add_parser(DEL_LOG_CMD, help="Move the project-tools log file to the trash.")
    delete_log_parser.set_defaults(func=delete_log.run)

    init_cli_parser = subparsers.add_parser(INIT_CLI_CMD, help="Setup new py cli project.")
    init_cli_parser.set_defaults(func=init_cli.run)
    for arg in ARGS[INIT_CLI_CMD]:
        create_command_args(init_cli_parser, arg)
    
    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        parser.exit()

    args.func(args)


def create_command_args(parser: argparse.ArgumentParser, model: ArgsModel):
    parser.add_argument(
        model.short_flag,
        model.flag,
        required = model.required,
        help = model.help,
    )
