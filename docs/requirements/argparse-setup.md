## Argparse Setup

### Constants

* Create file `src/project_tools/const.py`
* Add `WORKSPACE_PATH: Final[Path] = Path("/home/atari-monk/atari-monk/project")`
* Add `DEL_LOG_CMD: Final[str] = "del_log"`

### Argparse

* Create file `src/project_tools/argparse-setup.py`
* Add `setup_argparse() -> None`
* Create parser, subparsers for command, and parsers for commands
* Parse args
* Print help when no command is given and exit parser
* Run commands with args, use table `COMMANDS[args.command]()`

### Logger

* Import py logging
* Add `setup_logger(log_folder_path: Path, log_file_name: str) -> None`
* Default level info
* Format - timestamp, level, message
* Handle terminal and file log 

### [Delete log command](command/delete-log.md)

### Main

* In `main() -> None`
* Use modules to:
* Create foler `WORKSPACE_PATH / "log"`
* Setup logger with `WORKSPACE_PATH / "log" / "project-tools.log"`
* Setup argparse

---

Commit: `feat: argparse setup`
