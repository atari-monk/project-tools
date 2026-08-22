import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

from project_tools.const import BUNDLE_CMD, DEL_LOG_CMD, DEL_PROJ_CMD, GEN_IDX_CMD, GEN_IDX_ORDER_CMD, INIT_CLI_CMD, TIMER_CMD, SET_STR_CMD
from project_tools.command import bundle, delete_log, delete_project, generate_index, generate_index_order, setup_cli_project, setup_structure, timer


@dataclass(frozen=True)
class ArgsModel:
    short_flag: str
    flag: str
    required: bool
    help: str
    action: str | None = None
    dest: str | None = None
    default: Any = None
    nargs: str | int | None = None
    type: Callable[[str], Any] | None = None


ARGS = {
    DEL_LOG_CMD: [],
    INIT_CLI_CMD: [ArgsModel(short_flag = "-p", flag = "--project", required = True, help = "Project name"),
                   ArgsModel(short_flag = "-d", flag = "--description", required = True, help = "Project description"),
                   ArgsModel(short_flag = "-n", flag = "--cli_name", required = True, help = "CLI name"),
                   ArgsModel(short_flag = "-t", flag = "--page_title", required = True, help = "Page title")],
    DEL_PROJ_CMD: [ArgsModel(short_flag = "-p", flag = "--project", required = True, help = "Project name")],
    GEN_IDX_ORDER_CMD: [ArgsModel(short_flag = "-p", flag = "--project", required = True, help = "Project name")],
    GEN_IDX_CMD: [ArgsModel(short_flag = "-p", flag = "--project", required = True, help = "Project name")],
    TIMER_CMD: [
        ArgsModel(
            short_flag="-t",
            flag="--time",
            required=False,
            help="Time to count down, e.g. 5s, 25m or 1h",
        ),
        ArgsModel(
            short_flag="-o",
            flag="--pomodoro",
            required=False,
            action="store_true",
            default=False,
            help="Run a 25 minute pomodoro timer",
        ),
        ArgsModel(
            short_flag="-p",
            flag="--print",
            required=False,
            action="store_true",
            dest="print_log",
            default=False,
            help="Print the timer log",
        ),
        ArgsModel(
            short_flag="-e",
            flag="--edit",
            required=False,
            action="store_true",
            default=False,
            help="Open the timer log in Visual Studio Code",
        )
    ],
    SET_STR_CMD: [ArgsModel(short_flag = "-p", flag = "--project", required = True, help = "Project name")],
    BUNDLE_CMD: [
        ArgsModel(
            short_flag="-o",
            flag="--out",
            required=True,
            type=Path,
            help="Path to output markdown file",
        ),
        ArgsModel(
            short_flag="-p",
            flag="--paths",
            required=True,
            nargs="+",
            type=Path,
            help="Paths to process",
    )]
}


def setup_argparse() -> None:
    parser = argparse.ArgumentParser( 
        prog="project-tools",
        description="Project maintenance tools.")

    subparsers = parser.add_subparsers(dest="command", metavar="COMMAND",)

    del_log_parser = subparsers.add_parser(DEL_LOG_CMD, help="Move the project-tools log file to the trash.")
    create_command_args(del_log_parser, DEL_LOG_CMD, delete_log.run)

    init_cli_parser = subparsers.add_parser(INIT_CLI_CMD, help="Setup new py cli project.")
    create_command_args(init_cli_parser, INIT_CLI_CMD, setup_cli_project.run)

    del_proj_parser = subparsers.add_parser(DEL_PROJ_CMD, help="Move the project to the trash.")
    create_command_args(del_proj_parser, DEL_PROJ_CMD, delete_project.run)

    gen_idx_order_parser = subparsers.add_parser(GEN_IDX_ORDER_CMD, help="Generate docs index order for project.")
    create_command_args(gen_idx_order_parser, GEN_IDX_ORDER_CMD, generate_index_order.run)

    gen_idx_parser = subparsers.add_parser(GEN_IDX_CMD, help="Generate docs index for project.")
    create_command_args(gen_idx_parser, GEN_IDX_CMD, generate_index.run)

    timer_parser = subparsers.add_parser(TIMER_CMD, help="Timer to count down given time interval.")
    create_command_args(timer_parser, TIMER_CMD, timer.run)

    set_str_parser = subparsers.add_parser(SET_STR_CMD, help="Setup file structure of a project.")
    create_command_args(set_str_parser, SET_STR_CMD, setup_structure.run)

    bundle_parser = subparsers.add_parser(BUNDLE_CMD, help="Bundle files.")
    create_command_args(bundle_parser, BUNDLE_CMD, bundle.run)
    
    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        parser.exit()

    args.func(args)


def create_command_arg(
    parser: argparse.ArgumentParser,
    model: ArgsModel,
) -> None:
    kwargs: dict[str, Any] = {
        "required": model.required,
        "help": model.help,
    }

    if model.action is not None:
        kwargs["action"] = model.action

    if model.dest is not None:
        kwargs["dest"] = model.dest

    if model.default is not None:
        kwargs["default"] = model.default

    if model.nargs is not None:
        kwargs["nargs"] = model.nargs

    if model.type is not None:
        kwargs["type"] = model.type

    parser.add_argument(
        model.short_flag,
        model.flag,
        **kwargs,
    )


def create_command_args(
    parser: argparse.ArgumentParser,
    command: str,
    func: Callable[[argparse.Namespace], None],
) -> None:
    parser.set_defaults(func=func,
        parser=parser)

    for arg in ARGS[command]:
        create_command_arg(parser, arg)
