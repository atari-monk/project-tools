## Bundle Helper

### Prompt

/home/atari-monk/atari-monk/project/project-tools/prompt/prompt.md

### Data

/home/atari-monk/atari-monk/project/project-tools/data/commands.yaml

### Timer

/home/atari-monk/atari-monk/project/project-tools/docs/software-requirements-specification/command/timer.md
/home/atari-monk/atari-monk/project/project-tools/src/project_tools/command/timer.py
/home/atari-monk/atari-monk/project/project-tools/src/project_tools/modules/timer

### Note

/home/atari-monk/atari-monk/project/project-tools/docs/software-requirements-specification/command/note.md
/home/atari-monk/atari-monk/project/project-tools/src/project_tools/command/note.py
/home/atari-monk/atari-monk/project/project-tools/src/project_tools/modules/note

### Docs

#### Print

/home/atari-monk/atari-monk/project/project-tools/docs/software-requirements-specification/command/docs/print.md

#### New doc

/home/atari-monk/atari-monk/project/project-tools/docs/software-requirements-specification/command/docs/new-doc.md

#### Generate Index

/home/atari-monk/atari-monk/project/project-tools/docs/software-requirements-specification/command/docs/generate-index.md
/home/atari-monk/atari-monk/project/project-tools/src/project_tools/command/docs/generate_index.py
/home/atari-monk/atari-monk/project/project-tools/src/project_tools/modules/docs

### Shared

/home/atari-monk/atari-monk/project/project-tools/src/project_tools/shared/logger.py

### Bundle Command

#### Timer Logger

```sh
proj files bundle \
  -o /home/atari-monk/atari-monk/project/project-tools/prompt/prompt.md \
  -p /home/atari-monk/atari-monk/project/project-tools/docs/software-requirements-specification/command/timer.md \
  /home/atari-monk/atari-monk/project/project-tools/src/project_tools/command/timer.py \
  /home/atari-monk/atari-monk/project/project-tools/src/project_tools/modules/timer \
  /home/atari-monk/atari-monk/project/project-tools/src/project_tools/shared/logger.py
```

#### Docs

##### Print

```sh
proj files bundle \
  -o /home/atari-monk/atari-monk/project/project-tools/prompt/prompt.md \
  -p /home/atari-monk/atari-monk/project/project-tools/docs/software-requirements-specification/command/docs/print.md \
  /home/atari-monk/atari-monk/project/project-tools/data/commands.yaml \
  /home/atari-monk/atari-monk/project/project-tools/src/project_tools/modules/docs \
  /home/atari-monk/atari-monk/project/project-tools/src/project_tools/command/docs/generate_index.py
```

##### New doc

```sh
proj files bundle \
  -o /home/atari-monk/atari-monk/project/project-tools/prompt/prompt.md \
  -p /home/atari-monk/atari-monk/project/project-tools/docs/software-requirements-specification/command/docs/new-doc.md
```

##### Generate Index in any folder

```sh
proj files bundle \
  -o /home/atari-monk/atari-monk/project/project-tools/prompt/prompt.md \
  -p /home/atari-monk/atari-monk/project/project-tools/docs/software-requirements-specification/command/docs/generate-index.md \
  /home/atari-monk/atari-monk/project/project-tools/src/project_tools/command/docs/generate_index.py \
  /home/atari-monk/atari-monk/project/project-tools/src/project_tools/modules/docs
```