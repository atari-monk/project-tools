## Init Cli Command Setup

### Const

- Add `INIT_CLI_CMD` const with value `init_cli`
- Use type `Final[str]`

### File System

- Add function `create_folder_and_log_it(parent_path: Path, folder_name: str, logger: Logger) -> None`
- Add function `create_file_and_log_it(parent_path: Path, file_name: str, logger: Logger) -> None`
- Use `create_folder` or `create_file` and `log_file_system_result`

### Command

- Create file `src/project_tools/command/init_cli_cmd.py`
- Init module logger `logger = logging.getLogger(__name__)
- Create function `run(args: Namespace) -> None`
- Create project folder in `WORKSPACE_PATH`, named `args.project`
- Use `create_folder_and_log_it`

### Argparse setup

- Add dataclass `ArgsModel` with short_flag, flag, required and help
- Add table `ARGS` with key `INIT_CLI_CMD` and value of ArgsModel items array for init_cli command
- Command format: `proj init_cli -p project -d description -n cli_name -t page_title`
- Also use flag name: `--project, --description, --cli_name, --page_title`
- Add subparser for command, name it with command constant, set help
- Use `set_defaults(func=init_cli_cmd.run)` to set command func
- Create function `create_command_args(parser: argparse.ArgumentParser, model: ArgsModel)` - it adds argument to parser using model data
- Use for loop to set all args from `ARGS[INIT_CLI_CMD]` with `create_command_args`
- Run commands with `args.func(args)`

---

Commit: `feat: add init cli command`
