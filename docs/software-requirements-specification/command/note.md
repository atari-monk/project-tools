## Note

### Command

* Setup boilerplate code for command `proj note -l log_name -t "some text"`
* Add arg -l and --log alias
* Add arg -t and --text alias
* Add flag -p and --print alias

### Config

* Create json with log file names
* `/home/atari-monk/atari-monk/project/project-tools/data/note-logs.json`
* Flag -p prints out these as options
* Load this config
* Arg -l must be one of these log names

### Behavior

* Point of this command is to log text using cli app logger
* Logger uses its app config
* Additionally it logs to a file with log_name

### Helpers

* Implement structs and functions in `/home/atari-monk/atari-monk/project/project-tools/src/project_tools/modules/note`
* Use them in command

### Custom Logger

* Logger for this command must be a reference from project-tools app when -l arg is `project-tools`
    * In this situation use app logger and its log file
* Otherwise setup independent logger in command with a file from -l arg and to console aswell