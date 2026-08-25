## Delete project

### Constants

* Add const `DEL_PROJ_CMD` with value `del_proj`
* Use type Final[str]

### Command

* Create file `src/project_tools/command/delete_project.py`
* Set path `WORKSPACE_PATH / "project_name"`
* Log `Moving project: %s to trash`
* Check if path exists
* Log if not
* If so run `subprocess.run(["gio", "trash", str(path)], check=True)`, to move it to trash on ubuntu
* Log `Log project moved to trash`

### Argparse Setup

* Define args config in ARGS table under key DEL_PROJ_CMD with array of ArgsModel
* Add subparser for command with name (DEL_PROJ_CMD) and help
* Use `create_command_args`

### Commit

* feat: delete project