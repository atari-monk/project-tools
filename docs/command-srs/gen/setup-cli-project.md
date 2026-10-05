## Setup CLI project

Cli app command, to setup pyhon cli project configuration

### Const

- add `PYRIGHT_CONFIG` constant with `pyrightconfig.json` content
  - use type Final[dict[str, object]]
- add `INIT_MAIN` constant with hello world
  - use type Final[str]
- add function `get_page_title(project_name: str) -> str`
  - converts `some-name` to `Some Name`, to get page title

### Generator

- create file `generator.py`
- add function `set_pyright_config(project_name: str) -> FileSystemResult`
  - create project path from `WORKSPACE_PATH / project_name`
  - use `PYRIGHT_CONFIG` with `json.dumps` to generate content
  - use `create_file` to save content in file `pyrightconfig.json`
- add function `set_pyproject_toml(project_name: str, description: str, cli_name: str,) -> FileSystemResult`
  - set content with parametrized tripple double quotes string
  - use `create_file` to save it to `pyproject.toml`
- add function `set_gitignore`
  - set parent folder path
  - get package name from project name, replace - with \_
  - set content with parametrized tripple double quotes string
  - use `create_file` to save it to `.gitignore`

### Setup cli project

- create the file `src/project_tools/command/setup_cli_project.py`
- sdd function `run(args: Namespace) -> None`
- set project path to `WORKSPACE_PATH / args.project`
- set package name from project name, replace - with \_
- use `create_folder_with_logging` and `create_file_with_logging`
- create project folder
- generate `pyproject.toml`
- generate `pyrightconfig.json`
- generate `.gitignore`
- create `src` folder
- create `src/package_name` folder
- create `src/package_name/cli.py` file with hello world
- create `docs` folder
- create `docs/_config.yml` file
- create `docs/requirements`folder

### Setup Argparse

- command: `proj init_cli -p project -d description -n cli_name -t page_title`
- use flag name: `--project, --description, --cli_name, --page_title`
- feat: setup cli project
