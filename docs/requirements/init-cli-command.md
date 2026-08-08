## Init Cli Command

### Const

* Add `PYRIGHT_CONFIG` constant with `pyrightconfig.json` content
* Use type Final[dict[str, object]]
* Add `INIT_MAIN` constant with hello world
* Use type Final[str]
* Add function `get_page_title(project_name: str) -> str`
* It converts `some-name` to `Some Name`, to get page title 

### File system

* Fix create_file, it was creating empty file with touch
* Fix header to `create_file(parent_path: Path, file_name: str, content:str = "") -> FileSystemResult`
* Use `write_text` with content
* Rename helpers to `create_folder_with_logging` and `create_file_with_logging` and use content arg

### Generator

* Create file `generator.py`
* Add function `set_pyright_config(project_name: str) -> FileSystemResult`
* Create project path from `WORKSPACE_PATH / project_name`
* Use `PYRIGHT_CONFIG` with `json.dumps` to generate content
* Use `create_file` to save content in file `pyrightconfig.json`
* Add function `set_pyproject_toml(project_name: str, description: str, cli_name: str,) -> FileSystemResult`
* Set content with parametrized tripple double quotes string
* Use `create_file` to save it to `pyproject.toml`
* Add function `set_gitignore`
* Set parent folder path
* Get package name from project name, replace - with _
* Set content with parametrized tripple double quotes string
* Use `create_file` to save it to `.gitignore`

### Init Cli Command

* Add py module logger `logger = logging.getLogger(__name__)`
* Add function `run(args: Namespace) -> None`
* Set project path to `WORKSPACE_PATH / args.project`
* Set package name from project name, replace - with _
* Use `create_folder_with_logging` and `create_file_with_logging`
* Create project folder
* Generate `pyproject.toml`
* Generate `pyrightconfig.json`
* Generate `.gitignore`
* Create `src` folder
* Create `src/package_name` folder
* Create `src/package_name/cli.py` file with hello world
* Create `docs` folder
* Create `docs/_config.yml` file
* Create `docs/requirements`folder

---

Commit: `feat: init cli command`
