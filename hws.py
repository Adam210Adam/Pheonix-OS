from boot.osm import *
import os as oss
path = "~"
while True:
    _command = input(f"Path: {path}>> ")
    command_ARGS = _command.split(" ")
    command = command_ARGS[0]
    arguments = command_ARGS[1:]
    if command == "exit":
        exit()
    elif "exit" in command:
          print("Perhaps, have you added a extra letter")
    elif command == "uninstall":
                modules2 = ["calendar", "mistune", "sre_constants", "IPython", "certifi", "mmap", "sre_parse", "PIL", "cffi", "ssl", "PyInstaller", "PyQt5"]
                for moduleu in modules2:
                    oss.system(f"pip uninstall {moduleu}")
                    print(f"Uninstalling | {moduleu}")
    elif "unistall" in command:
          print("Perhaps, have you added a extra letter")
    else:
        class bcolors:
                HEADER = '\033[95m'
                OKBLUE = '\033[94m'
                OKCYAN = '\033[96m'
                OKGREEN = '\033[92m'
                WARNING = '\033[93m'
                FAIL = '\033[91m'
                ENDC = '\033[0m'
                BOLD = '\033[1m'
                UNDERLINE = '\033[4m'
        print(bcolors.FAIL + f"{_command}")
        print("~" * len(_command))
        print(f"Unexpected Syntax: {_command}" + bcolors.ENDC)