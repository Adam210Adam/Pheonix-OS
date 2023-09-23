from _sdl import infos
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
task = 0
for inf in infos:
    if task == 5:
        import os
        os.system("python osDrivers.py")
    if inf.name == "clast":
        if inf.value == 17.9:
            print(bcolors.OKGREEN + "INFO: C VERSION MATCHED" + bcolors.ENDC)
        elif inf.value > 17.9:
            print(bcolors.WARNING + "WARNING: C VERSION GREATER THAN 17.9 VISIT ??? to learn more." + bcolors.ENDC)
        elif inf.value < 17.9:
            print(bcolors.FAIL + "ERROR: FAILED RUNNING OPERATING SYSTEM")
            print("C VERSION LESS THAN 17.9" + bcolors.ENDC)
        task += 1
    elif inf.name == "pylast":
        if inf.value == 3.11:
            print(bcolors.OKGREEN + "INFO: PYTHON VERSION MATCHED" + bcolors.ENDC)
        elif inf.value > 3.11:
            print(bcolors.WARNING + "WARNING: PYTHON VERSION GREATER THAN 3.11 VISIT ??? to learn more." + bcolors.ENDC)
        elif inf.value < 3.11:
            print(bcolors.FAIL + "ERROR: FAILED RUNNING OPERATING SYSTEM")
            print("PYTHON VERSION LESS THAN 3.11" + bcolors.ENDC)
        task += 1
    elif inf.name == "rubylast":
        if inf.value == 38.9:
            print(bcolors.OKGREEN + "INFO: RUBY VERSION MATCHED" + bcolors.ENDC)
        elif inf.value > 38.9:
            print(bcolors.WARNING + "WARNING: RUBY VERSION GREATER THAN 38.9 VISIT ??? to learn more." + bcolors.ENDC)
        elif inf.value < 38.9:
            print(bcolors.FAIL + "ERROR: FAILED RUNNING OPERATING SYSTEM")
            print("C VERSION LESS THAN 38.9" + bcolors.ENDC)
        task += 1
    elif inf.name == "vsllast":
        if inf.value == 0.1:
            print(bcolors.OKGREEN + "INFO: VSL VERSION MATCHED" + bcolors.ENDC)
        elif inf.value > 0.1:
            print(bcolors.WARNING + "WARNING: VSL VERSION GREATER THAN 0.1 VISIT ??? to learn more." + bcolors.ENDC)
        elif inf.value < 0.1:
            print(bcolors.FAIL + "ERROR: FAILED RUNNING OPERATING SYSTEM")
            print("VSL VERSION LESS THAN 0.1" + bcolors.ENDC)
        task += 1