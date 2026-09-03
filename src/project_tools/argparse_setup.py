from pathlib import Path
from typing import Any
import argparse
from project_tools.spec import ArgumentSpec, CommandSpec
from project_tools.spec_loader import load_command_specs
from project_tools.command import (
    bundle,
    delete_log,
    delete_project,
    generate_atom_game,
    generate_index,
    generate_index_order,
    generate_py_cli,
    note,
    setup_structure,
    timer,
)


ARG_TYPES = {
    "path": Path,
    "str": str,
    "int": int,
    "float": float,
}


def resolve_arg_type(type_name: str | None) -> Any:
    if type_name is None:
        return None

    try:
        return ARG_TYPES[type_name]
    except KeyError as exc:
        raise ValueError(
            f"Unknown argument type: {type_name}"
        ) from exc


COMMAND_FUNCTIONS = {
    "bundle.run": bundle.run,
    "delete_log.run": delete_log.run,
    "delete_project.run": delete_project.run,
    "generate_atom_game.run": generate_atom_game.run,
    "generate_index.run": generate_index.run,
    "generate_index_order.run": generate_index_order.run,
    "generate_py_cli.run": generate_py_cli.run,
    "note.run": note.run,
    "setup_structure.run": setup_structure.run,
    "timer.run": timer.run,
}


def resolve_function(function_name: str):
    try:
        return COMMAND_FUNCTIONS[function_name]
    except KeyError as exc:
        raise ValueError(
            f"Unknown command function: {function_name}"
        ) from exc


def create_command_arg(
    parser: argparse.ArgumentParser,
    model: ArgumentSpec,
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
        kwargs["type"] = resolve_arg_type(model.type)

    parser.add_argument(
        model.short_flag,
        model.flag,
        **kwargs,
    )


def create_command_args(
        parser: argparse.ArgumentParser,
        command: CommandSpec,
    ) -> None:
        parser.set_defaults(
            func=resolve_function(command.function),
        )

        for arg in command.args:
            create_command_arg(parser, arg)


COMMANDS_FILE = Path("/home/atari-monk/atari-monk/project/project-tools/data/commands.yaml")


def setup_argparse() -> None:
    parser = argparse.ArgumentParser( 
        prog="project-tools",
        description="Project maintenance tools.")

    subparsers = parser.add_subparsers(dest="command", metavar="COMMAND",)

    commands = load_command_specs(COMMANDS_FILE)

    for command in commands:
        command_parser = subparsers.add_parser(
            command.name,
            help=command.help,
        )

        create_command_args(
            command_parser,
            command,
        )
    
    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        parser.exit()

    args.func(args)