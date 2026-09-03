from pathlib import Path

from project_tools.spec_loader import load_command_specs


commands = load_command_specs(Path("/home/atari-monk/atari-monk/project/project-tools/data/commands.yaml"))

for command in commands:
    print(command.name, command.function)

    for child in command.commands:
        print("  ", child.name, child.function)