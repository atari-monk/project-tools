## Delete project

- feat: delete project
- create file `src/project_tools/command/files/delete_project.py`
- set path `WORKSPACE_PATH / "project_name"`
- log `Moving project: %s to trash`
- check if path exists
- log if not
- if so run `subprocess.run(["gio", "trash", str(path)], check=True)`, to move it to trash on ubuntu
- log `Log project moved to trash`
