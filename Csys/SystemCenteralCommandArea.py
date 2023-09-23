path = "~"
while True:
    _command = input(f"Path: {path}>> ")
    command_ARGS = _command.split(" ")
    command = command_ARGS[0]
    arguments = command_ARGS[1:]
    if command == "exit":
        exit()
    elif command == "uninstall" and arguments[0] == "System" and arguments[1] == "LIB":
        if unistallExecuted == "unistall" and Permission == 3:
                for moduleu in modules2:
                    os.system(f"pip uninstall {moduleu}")
                    print(f"Uninstalling | {moduleu}")
            elif unistallExecuted == "unistall" and Permission == 1 or Permission == 2:
                print("No Permission To unistall System Libraries")