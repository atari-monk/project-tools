## Argparse Setup

Argparse setup for cli app with commands.

### Argparse

* Create file `src/project_tools/argparse-setup.py`
* Add `setup_argparse() -> None`
* Create parser, set prog and description props
* Create subparsers container for command, set dest and metavar props
* dest - is selected command `args.command`
* metavar is parser name printed in help
* Create parsers for commands
* Parse args
* Print help when no command is given and exit parser
* Run commands with args, use `args.func(args)`

### Helpers

* Add dataclass `ArgsModel` with short_flag, flag, required and help
* Add table `ARGS` with keys `NAME_CMD` and value of ArgsModel items array for each command
* Add subparser for command, name it with command constant, set help
* Use `set_defaults(func=name_cmd.run)` to set command func
* Create function `create_command_arg(parser: argparse.ArgumentParser, model: ArgsModel)` - it adds argument to parser using model data
* Create function `create_command_args`
* Set default python function for parser with `parser.set_defaults(func=func)` 
* Use for loop to set all args from `ARGS[NAME_CMD]` with `create_command_arg`

### Commits

* feat: argparse setup
* feat: init cli command setup