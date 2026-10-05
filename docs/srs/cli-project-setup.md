## CLI Project Setup

Minimalistic file structure for CLI python project

### Project Config File

- create `pyproject.toml`
  - configure the `build-system`
  - set the project name, version, and description
  - define terminal command
  - use `src` as the source root

### Hello World Entrypoint

- create the package `src/package_name`
- add `src/package_name/cli.py` with Hello World

### Docs

- create folder `docs`
- create \_config.yml with github page title
- create folder `srs`
- create order and index files with cli

### Gitignore

- add `.gitignore`

For example:

```
__pycache__
project_name.egg-info
.venv/
.ruff_cache/
prompt
```

### [Install CLI](https://atari-monk.github.io/dev-notes/en/python/install-cli.html)

- test cli hello world in terminal

### Commit message

- chore: project setup

---

[TTS](../text-to-speech/cli-project-setup.txt)
