## Minimal Setup

### Project config

* Create `pyproject.toml`
* Configure the `build-system`
* Set the project name, version, and description
* Define the `proj` terminal command
* Use `src` as the source root

### Hello world

* Create the `src/project_tools` package
* Add `src/project_tools/cli.py` with Hello World

### Install

Install cli script globally and test (ubuntu).

```sh
# install pipx
sudo apt install pipx
pipx ensurepath

# install cli
deactivate

pipx uninstall proj
pipx install -e .
```

### Docs

* Create folders `docs/requirements/minimal-setup.md`
* Create _config.yml with github page title
* Create `index.md`

### Gitignore

Add `.gitignore` with pycache and egg-info.  
Commit `chore: project setup`.
