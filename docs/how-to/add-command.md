## How to add command to project-tools cli

### 1. Add command name 

In path `src/project_tools/const.py`, add a const for new command name.  
Value of this constant is a command name in cli.  
For example:

```py
DEL_LOG_CMD: Final[str] = "del_log"
```

### 2. Set command boilerplate for argparse

In path `src/project_tools/setup_argparse.py`, add command args data.  
Use empty array when no args.  
For example:

```py
ARGS = {
    DEL_LOG_CMD: [],
    INIT_CLI_CMD: [ArgsModel(short_flag = "-p", flag = "--project", required = True, help = "Project name"),
                   ArgsModel(short_flag = "-d", flag = "--description", required = True, help = "Project description")]

}
```

Add these lines:

```py
del_proj_parser = subparsers.add_parser(DEL_PROJ_CMD, help="Move the project to the trash.")
create_command_args(del_proj_parser, DEL_PROJ_CMD, delete_proj.run)
```

### 3. Add command file

In path `src/project_tools/command` add a file with command named `verb_noun.py`.  
For example `delete_log.py`.  

Command has its interface/pattern:

```py
from argparse import Namespace
import logging

from project_tools.const import WORKSPACE_PATH


logger = logging.getLogger(__name__)


def run(args: Namespace) -> None:
    logger.info("Workspace: %s", WORKSPACE_PATH)
```
