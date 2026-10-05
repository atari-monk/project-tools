## Argparse Setup

Argparse setup for cli app with commands (Obsolete)

### Argparse

- create file `src/project_tools/argparse-setup.py`
- add `setup_argparse() -> None`
  - create parser, set prog and description props
  - create subparsers container for command, set dest and metavar props
    - dest - is selected command `args.command`
    - metavar is parser name printed in help
  - Create parsers for commands
  - Parse args
  - Print help when no command is given and exit parser
  - Run commands with args, use `args.func(args)`

### Helpers

- add dataclass `ArgsModel` with short_flag, flag, required and help
- add table `ARGS` with keys `NAME_CMD` and value of ArgsModel items array for each command
- add subparser for command, name it with command constant, set help
- use `set_defaults(func=name_cmd.run)` to set command func
- create function `create_command_arg(parser: argparse.ArgumentParser, model: ArgsModel)` - it adds argument to parser using model data
- create function `create_command_args`
- set default python function for parser with `parser.set_defaults(func=func)`
- use for loop to set all args from `ARGS[NAME_CMD]` with `create_command_arg`
- feat: argparse setup
