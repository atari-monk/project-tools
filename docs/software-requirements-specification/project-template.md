## Project Template

Minimalistic file structure for python project.

### Project Config File

* Create `pyproject.toml`
* Configure the `build-system`
* Set the project name, version, and description
* Define terminal command
* Use `src` as the source root

### Hello World Entrypoint

* Create the package `src/package_name`
* Add `src/package_name/cli.py` with Hello World

### Install CLI

Install cli script globally (ubuntu).

Command Set:

```sh
# install pipx
sudo apt install pipx
pipx ensurepath

# deactivate virtual environment
deactivate

# uninstall cli
pipx uninstall cli-name

# install cli
pipx install -e .
```

### Docs

* Create folder `docs`
* Create _config.yml with github page title
* Create folder `software-requirements-specification`
* Create `index.md`

### Gitignore

* Add `.gitignore`

For example:

```
__pycache__
project_name.egg-info
.venv/
.ruff_cache/
temp
```

### Commits

* chore: project setup