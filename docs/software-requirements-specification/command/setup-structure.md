## Setup Structure

### Data model

* Design data to create project structure
* Name - id to select project
* Project path - path to folder of a project
* Folders array - list of folders of a project
* Files array - list of files of a project

### Data format

* Create simplest and best suited data file for data model
* Make empty schema
* Make some example to test it

### Goal

* Task is to create file structure of a project given its data

### Implementation

* Implement helper functions for loading data to memory data model
* Helper functions to create project structure
* Orcherstrator function `create-project(name:str, logger: Logger)-> None`
* `src/project_tools/shared/setup-structure` is container for data model, helpers and orchestrator
* `/home/atari-monk/atari-monk/project/project-tools/data` is container for data

### Commits

* feat: setup structure 