### Delete Log Command

* Create file `src/project_tools/command/delete_log.py`
* Set path `WORKSPACE_PATH / "log" / "project-tools.log"`
* Log `Moving log: %s to trash`
* Check if path exists
* If so run `subprocess.run(["gio", "trash", str(path)], check=True)`, to move it to trash on ubuntu
* Log `Log file moved to trash`