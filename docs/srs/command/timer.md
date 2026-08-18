## Timer

### Argparse setup

* Setup command boilerplate for `proj timer -t 25m`.
* -t arg accepts a time string like `5s or 1h or 25m`.
* Add --time alias.
- -o flag runs timer for pomodoro with 25m set.
* Add --pomodoro alias.
* -p flag prints log file to console.
* Add --print alias.
* -e flag opens log file in visual studio code to edit.
* `code <log-file>`
* Add --edit alias.
* All args/flags are optional

### Logger

* Setup logger for this command.
* Use console and file.
* File path is `/home/atari-monk/atari-monk/project/log/timer.log`.

### Behavior

* Log start timestamp.
* Run timer asynchronously/backgrounded while the CLI remains usable.
* When timer runs down log stop timestamp.
* Use consistent format for logs:
```md
start yyyy-mm-dd hh:mm
stop yyyy-mm-dd hh:mm
```
* Use ubuntu notify pop up to signal timer end.
* Use sound on ubuntu to signal timer end.
* When no args or wrong args, print help

### Commits 

* feat: timer