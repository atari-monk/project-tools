# How to add a command to the project-tools CLI

Commands are defined in:

```text
data/commands.yaml
```

The CLI parser is generated from this file, so you normally **do not need to modify `argparse_setup.py`** when adding a command.

## 1. Add the command to `commands.yaml`

Add the command under the top-level `commands:` section.

For a command without arguments:

```yaml
commands:
  my_command:
    help: Description of my command.
    function: my_command.run
```

For a command with arguments:

```yaml
commands:
  my_command:
    help: Description of my command.
    function: my_command.run
    args:
      - short_flag: "-p"
        flag: "--project"
        required: true
        help: Project name
```

The `name` of the YAML entry becomes the command name in the CLI.

For example:

```yaml
commands:
  note:
    help: Note with logger.
    function: note.run
```

creates:

```text
proj note
```

### Argument fields

Arguments can contain the following fields:

| Field        | Description                                            |
| ------------ | ------------------------------------------------------ |
| `short_flag` | Short option such as `-p`                              |
| `flag`       | Long option such as `--project`                        |
| `required`   | Whether the argument is required                       |
| `help`       | Help text displayed by argparse                        |
| `action`     | argparse action, such as `store_true`                  |
| `dest`       | Optional argparse destination name                     |
| `default`    | Optional default value                                 |
| `nargs`      | Optional argparse `nargs` value                        |
| `type`       | Argument type such as `path`, `str`, `int`, or `float` |

For example:

```yaml
commands:
  my_command:
    help: Example command.
    function: my_command.run
    args:
      - short_flag: "-p"
        flag: "--project"
        required: true
        help: Project name

      - short_flag: "-v"
        flag: "--verbose"
        required: false
        action: store_true
        help: Enable verbose output
```

The CLI will then accept:

```bash
proj my_command -p project-tools
```

or:

```bash
proj my_command --project project-tools --verbose
```

## 2. Add the command implementation

Create a Python file in:

```text
src/project_tools/command/
```

The file should normally use the command's name.

For example:

```text
src/project_tools/command/my_command.py
```

The command implementation exposes a `run()` function:

```python
from argparse import Namespace

import logging


logger = logging.getLogger(__name__)


def run(args: Namespace) -> None:
    logger.info("Running my command")
```

Arguments defined in `commands.yaml` are available through `args`.

For example, with:

```yaml
args:
  - short_flag: "-p"
    flag: "--project"
    required: true
    help: Project name
```

the implementation can use:

```python
def run(args: Namespace) -> None:
    logger.info("Project: %s", args.project)
```

## 3. Register the command function

The YAML stores the function as a string:

```yaml
function: my_command.run
```

The corresponding Python function must be registered in the function registry in:

```text
src/project_tools/argparse_setup.py
```

Add an import:

```python
from project_tools.command import my_command
```

Then add the function to `COMMAND_FUNCTIONS`:

```python
COMMAND_FUNCTIONS = {
    # existing commands...

    "my_command.run": my_command.run,
}
```

The string in `commands.yaml` must exactly match the key in `COMMAND_FUNCTIONS`.

For example:

```yaml
function: my_command.run
```

matches:

```python
"my_command.run": my_command.run,
```

## 4. Add a nested command

Commands can also be grouped under another command.

For example, documentation commands are defined as:

```yaml
commands:
  docs:
    help: Documentation commands.
    commands:
      gen_idx_order:
        help: Generate docs index order for project.
        function: generate_index_order.run
        args:
          - short_flag: "-p"
            flag: "--project"
            required: true
            help: Project name

      gen_idx:
        help: Generate docs index for project.
        function: generate_index.run
        args:
          - short_flag: "-p"
            flag: "--project"
            required: true
            help: Project name
```

This creates:

```text
proj docs gen_idx
proj docs gen_idx_order
```

The group itself does not have a `function`:

```yaml
docs:
  help: Documentation commands.
  commands:
    ...
```

Only leaf commands have a `function`.

The parser automatically creates the nested command structure, so no additional argparse code is required.

## 5. Add argument types when needed

For arguments that need conversion, specify `type` in YAML.

Available types are currently:

```yaml
type: path
type: str
type: int
type: float
```

For example:

```yaml
args:
  - short_flag: "-n"
    flag: "--count"
    required: true
    help: Number of items
    type: int
```

This causes argparse to pass an `int` to the command implementation.

## 6. Test the command

After adding the command, check its help:

```bash
proj my_command --help
```

For a nested command:

```bash
proj docs --help
```

Then test the actual command:

```bash
proj my_command ...
```

For a nested command:

```bash
proj docs gen_idx --help
proj docs gen_idx -p project-tools
```

## Summary

When adding a normal command:

1. Add the command to `data/commands.yaml`.
2. Add its arguments to the YAML if needed.
3. Create `src/project_tools/command/<command>.py`.
4. Implement `run(args)`.
5. Add the function to `COMMAND_FUNCTIONS` in `argparse_setup.py`.
6. Test the command and its `--help`.

When adding a nested command, put it under a parent command's `commands:` section.

The important principle is:

```text
commands.yaml
    ↓
CommandSpec
    ↓
argparse
    ↓
COMMAND_FUNCTIONS
    ↓
command.run(args)
```