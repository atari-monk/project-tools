## Timer

### Argparse setup

* Setup boilerplate code for command:
```sh
proj timer -t 25m
```
* All args/flags are optional

#### Time Arg

* Arg `-t` accepts a time string like `5s or 1h or 25m`
* Add `--time` alias

#### Pomodoro flag

* `-o` flag runs timer for pomodoro with 25m set
* Add `--pomodoro` alias

#### Print flag

* `-p` flag prints log file to console
* Add `--print` alias

#### Edit flag

* `-e` flag opens log file in visual studio code to edit
* `code <log-file>`
* Add `--edit` alias

### Logger

* Setup a custom logger for this command
* Add a separate log file `/home/atari-monk/atari-monk/project/log/timer.log`
* Use `/home/atari-monk/atari-monk/project/project-tools/src/project_tools/shared/logger.py` `setup_custom_logger`
* The timer command logs to console and `timer.log`
* The background timer worker logs to `timer.log` only
* The timer worker must not write timer completion messages to the interactive terminal
* The timer logger must not propagate to the application logger
* Other commands must not log to `timer.log`

### Behavior

* Log info message: `Starting timer -t x`
* Run timer asynchronously/backgrounded while the CLI remains usable
* When timer runs down log `Stoping timer -t x`
* Use ubuntu notify pop up to signal timer end
* Use sound on ubuntu to signal timer end
* When no args or wrong args, print help

### Commits 

* feat: timer setup
* feat: implement timer functionality
* feat: implement timer logger
* fix: custom timer logger