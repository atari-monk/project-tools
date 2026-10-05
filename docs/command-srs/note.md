## Note

### Command

- command: `proj note -l log_name -t "some text"`
- add arg -l and --log alias
- add arg -t and --text alias
- add flag -p and --print alias

### Config

- create json with log file names
- `data/note-logs.json`
- flag -p prints out these as options
- load this config
- arg -l must be one of these log names

### Behavior

- point of this command is to log text using cli app logger
- logger uses its app config
- additionally it logs to a file with log_name

### Helpers

- implement structs and functions in `src/project_tools/modules/note`
- use them in command

### Custom Logger

- logger for this command must be a reference from project-tools app when -l arg is `project-tools`
  - in this situation use app logger and its log file
- otherwise setup independent logger in command with a file from -l arg and to console

---

[TTS](../text-to-speech/note.txt)
