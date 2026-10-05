## Setup Structure

### Data model

- design data to create project structure
- name - id to select project
- project path - path to folder of a project
- folders array - list of folders of a project
- files array - list of files of a project

### Data format

- create simplest and best suited data file for data model
- make empty schema
- make some example to test it

### Goal

- task is to create file structure of a project given its data

### Implementation

- implement helper functions for loading data to memory data model
- helper functions to create project structure
- orcherstrator function `create-project(name:str, logger: Logger)-> None`
- use folder `src/project_tools/modules/setup_structure` for helpers
- use folder `/home/atari-monk/atari-monk/project/project-tools/data` for data
- feat: setup structure
