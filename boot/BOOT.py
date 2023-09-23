import os
import time
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
for boot in range(1, 101):
    if boot != 10 or not boot > 10 and boot != 100:
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                                                                |")
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                                                                |")
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                                                                |")
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                                                                |")
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                   Pheonix OS                                   |")
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                                                                |")
        print(bcolors.BOLD + bcolors.OKGREEN + f"|                                {boot}%                                              |")
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                                                                |")
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                                                                |")
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                                                                |")
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                                                                |")
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                                                                |" + bcolors.ENDC)
    elif boot == 10 or boot > 10:
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                                                                |")
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                                                                |")
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                                                                |")
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                                                                |")
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                   Pheonix OS                                   |")
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                                                                |")
        print(bcolors.BOLD + bcolors.OKGREEN + f"|                                {boot}%                                             |")
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                                                                |")
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                                                                |")
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                                                                |")
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                                                                |")
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                                                                |" + bcolors.ENDC)
    elif boot == 100:
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                                                                |")
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                                                                |")
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                                                                |")
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                                                                |")
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                   Pheonix OS                                   |")
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                                                                |")
        print(bcolors.BOLD + bcolors.OKGREEN + f"|                               {boot}%                                           |")
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                                                                |")
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                                                                |")
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                                                                |")
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                                                                |")
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                                                                |" + bcolors.ENDC)
    else:
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                                                                |")
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                                                                |")
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                                                                |")
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                                                                |")
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                   Pheonix OS                                   |")
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                                                                |")
        print(bcolors.BOLD + bcolors.OKGREEN + f"|                               {boot}%                                              |")
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                                                                |")
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                                                                |")
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                                                                |")
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                                                                |")
        print(bcolors.BOLD + bcolors.OKGREEN + "|                                                                                |" + bcolors.ENDC)
    time.sleep(0.2)
    os.system("cls")