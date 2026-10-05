## Project `project-tools` structure

```text
/home/atari-monk/atari-monk/project/project-tools
├── data
│   ├── bundle.json
│   ├── commands.yaml
│   ├── note-logs.json
│   └── projects.json
├── docs
│   ├── command-srs
│   │   ├── docs
│   │   │   ├── generate-index.md
│   │   │   ├── generate-index-order.md
│   │   │   ├── new-doc.md
│   │   │   └── print.md
│   │   ├── files
│   │   │   ├── delete-project.md
│   │   │   ├── file-bundling.md
│   │   │   └── setup-structure.md
│   │   ├── gen
│   │   │   └── setup-cli-project.md
│   │   ├── note.md
│   │   └── timer.md
│   ├── _config.yml
│   ├── git-history.md
│   ├── index.md
│   ├── order.txt
│   ├── project-structure.md
│   ├── srs
│   │   ├── argparse-setup-v1.md
│   │   ├── argparse-setup-v2.md
│   │   ├── cli-project-setup.md
│   │   └── helpers.md
│   └── text-to-speech
│       └── cli-project-setup.txt
├── .gitignore
├── prompt
│   ├── command.md
│   ├── prompt.md
│   ├── srs.md
│   └── task.md
├── pyproject.toml
├── pyrightconfig.json
├── src
│   └── project_tools
│       ├── argparse_setup.py
│       ├── cli.py
│       ├── command
│       │   ├── docs
│       │   │   ├── generate_index_order.py
│       │   │   ├── generate_index.py
│       │   │   ├── new.py
│       │   │   └── print.py
│       │   ├── files
│       │   │   ├── bundle.py
│       │   │   ├── delete_project.py
│       │   │   └── setup_structure.py
│       │   ├── gen
│       │   │   ├── generate_atom_game.py
│       │   │   └── generate_py_cli.py
│       │   ├── note.py
│       │   └── timer.py
│       ├── config.py
│       ├── modules
│       │   ├── bundle
│       │   │   ├── bundler.py
│       │   │   ├── __init__.py
│       │   │   └── model.py
│       │   ├── docs
│       │   │   ├── discovery.py
│       │   │   ├── index.py
│       │   │   ├── index_render.py
│       │   │   ├── new.py
│       │   │   ├── order.py
│       │   │   └── print.py
│       │   ├── note
│       │   │   ├── config.py
│       │   │   └── __init__.py
│       │   ├── project_atom_game
│       │   │   ├── files.py
│       │   │   └── generator.py
│       │   ├── project_py_cli
│       │   │   ├── data_model.py
│       │   │   ├── files.py
│       │   │   └── generator.py
│       │   ├── project_shared
│       │   │   ├── data_model.py
│       │   │   ├── generator.py
│       │   │   ├── types.py
│       │   │   └── utils.py
│       │   ├── setup_structure
│       │   │   ├── creator.py
│       │   │   ├── __init__.py
│       │   │   ├── loader.py
│       │   │   ├── model.py
│       │   │   └── orchestrator.py
│       │   └── timer
│       │       ├── duration.py
│       │       ├── events.py
│       │       ├── __init__.py
│       │       ├── log.py
│       │       ├── notification.py
│       │       ├── runner.py
│       │       ├── sound.py
│       │       └── worker.py
│       ├── shared
│       │   ├── file_system.py
│       │   └── logger.py
│       ├── spec_loader.py
│       ├── spec.py
│       └── spec_test.py
└── tests
    └── shared
        └── setup_structure
            ├── test_creator.py
            ├── test_loader.py
            └── test_orchestrator.py

29 directories, 86 files
```

---

[TTS](text-to-speech/project-structure.txt)
