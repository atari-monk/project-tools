import argparse
from dataclasses import dataclass
from typing import Callable

from project_tools.const import DEL_LOG_CMD, DEL_PROJ_CMD, GEN_IDX_CMD, GEN_IDX_ORDER_CMD, INIT_CLI_CMD
from project_tools.command import del_log, del_proj, gen_idx, gen_idx_order, init_cli


@dataclass(frozen=True)
class ArgsModel:
    short_flag: str
    flag: str
    required: bool
    help: str


ARGS = {
    DEL_LOG_CMD: [],
    INIT_CLI_CMD: [ArgsModel(short_flag = "-p", flag = "--project", required = True, help = "Project name"),
                   ArgsModel(short_flag = "-d", flag = "--description", required = True, help = "Project description"),
                   ArgsModel(short_flag = "-n", flag = "--cli_name", required = True, help = "CLI name"),
                   ArgsModel(short_flag = "-t", flag = "--page_title", required = True, help = "Page title")],
    DEL_PROJ_CMD: [ArgsModel(short_flag = "-p", flag = "--project", required = True, help = "Project name")],
    GEN_IDX_ORDER_CMD: [ArgsModel(short_flag = "-p", flag = "--project", required = True, help = "Project name")],
    GEN_IDX_CMD: [ArgsModel(short_flag = "-p", flag = "--project", required = True, help = "Project name")]
}


def setup_argparse() -> None:
    parser = argparse.ArgumentParser( 
        prog="project-tools",
        description="Project maintenance tools.")

    subparsers = parser.add_subparsers(dest="command", metavar="COMMAND",)

    del_log_parser = subparsers.add_parser(DEL_LOG_CMD, help="Move the project-tools log file to the trash.")
    create_command_args(del_log_parser, DEL_LOG_CMD, del_log.run)

    init_cli_parser = subparsers.add_parser(INIT_CLI_CMD, help="Setup new py cli project.")
    create_command_args(init_cli_parser, INIT_CLI_CMD, init_cli.run)

    del_proj_parser = subparsers.add_parser(DEL_PROJ_CMD, help="Move the project to the trash.")
    create_command_args(del_proj_parser, DEL_PROJ_CMD, del_proj.run)

    gen_idx_order_parser = subparsers.add_parser(GEN_IDX_ORDER_CMD, help="Generate docs index order for project.")
    create_command_args(gen_idx_order_parser, GEN_IDX_ORDER_CMD, gen_idx_order.run)

    gen_idx_parser = subparsers.add_parser(GEN_IDX_CMD, help="Generate docs index for project.")
    create_command_args(gen_idx_parser, GEN_IDX_CMD, gen_idx.run)

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
