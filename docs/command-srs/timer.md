## Timer

### Argparse setup

- command: `proj timer -t 25m`
- all args/flags are optional
- arg `-t` accepts a time string like `5s or 1h or 25m`
  - add `--time` alias
- `-o` flag runs timer for pomodoro with 25m set
  - add `--pomodoro` alias
- `-p` flag prints log file to console
  - add `--print` alias
- `-e` flag opens log file in visual studio code to edit
  - `code <log-file>`
  - add `--edit` alias

### Logger

- setup a custom logger for this command
- add a separate log file `~/atari-monk/project/log/timer.log`
- use `src/project_tools/shared/logger.py` `setup_custom_logger`
- the timer command logs to console and `timer.log`
- the background timer worker logs to `timer.log` only
- the timer worker must not write timer completion messages to the interactive terminal
- the timer logger must not propagate to the application logger
- other commands must not log to `timer.log`

### Behavior

- log info message: `Starting timer -t x`
- run timer asynchronously/backgrounded while the CLI remains usable
- when timer runs down log `Stoping timer -t x`
- use ubuntu notify pop up to signal timer end
- use sound on ubuntu to signal timer end
- when no args or wrong args, print help
- feat: timer setup
