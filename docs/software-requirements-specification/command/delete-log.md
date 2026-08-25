## Delete log

Delete log file (`project-tools.log`).

### Constants

* Create file `src/project_tools/const.py`
* Add `WORKSPACE_PATH: Final[Path] = Path("/home/atari-monk/atari-monk/project")`
* Add `DEL_LOG_CMD: Final[str] = "del_log"`

### Command

* Create file `src/project_tools/command/delete_log.py`
* Set path `WORKSPACE_PATH / "log" / "project-tools.log"`
* Log `Moving log: %s to trash`
* Check if path exists
* If so run `subprocess.run(["gio", "trash", str(path)], check=True)`, to move it to trash on ubuntu
* Log `Log file moved to trash`