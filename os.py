# Welcome To the OS Manager

import os # System Commands
import hashlib # Hasher
import BooterDir.boot
import winsound

winsound.PlaySound('sound.wav', winsound.SND_FILENAME)

os.system(r"cd C:\Users\sch\Desktop\Pheonix OS") # Changing working directory such as (wd)

Cfile = hashlib.sha1("osCR".encode()).hexdigest()[0:5] # Hashed 0:5 Name of the Cfile
PythonFile = hashlib.sha1("osCpython".encode()).hexdigest()[0:5] # Hashed 0:5 Name of the Python File
try:
    # try to open the compiled version of osCR.c
    open(r"build\osCR.exe")
except:
    # if the compiled version of osCR.c was not found this code will run down bellow
    print("Creating File System")
    try:
        # trying to make a directory called build
        os.mkdir("build")
    except:
        # if the build directory already exists we do nothing
        pass
    os.system(r"gcc osCR.c Bootloader.c -o build\osCR.exe") # Compiling The C file 
def RunC_code():
        os.system(r"cd C:\Users\sch\Desktop\Pheonix OS") # Same as line 5
        os.system(r"build\osCR") # Running The Compiled version of the C code
print(f"{Cfile}: Successfully loaded C file")
print(f"{PythonFile}: Executing {Cfile}...")
BooterDir.boot.boot()
RunC_code()
input("Press Enter To exit the program... ")