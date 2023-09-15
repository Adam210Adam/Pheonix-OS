# Welcome To the OS Manager

import os # System Commands
import hashlib # Hasher
import BooterDir.boot
import winsound
import System0Loader.System16BitLoader


System0Loader.System16BitLoader.load()
os.system(r"cd C:\Users\sch\Desktop\Pheonix OS") # Changing working directory such as (wd)

Cfile = hashlib.sha1("osCR".encode()).hexdigest().capitalize()[0:5] # Hashed and Capatilizrd 0:5 Name of the Cfile
PythonFile = hashlib.sha1("osCpython".encode()).hexdigest().capitalize()[0:5] # Hashed And Capatalized 0:5 Name of the Python File
FileManager = hashlib.sha1("FileMaker/FileManager".encode()).hexdigest().capitalize()[0:5] # Hashed And Capatalized 0:5 Name of the Python File
try:
    # try to open the compiled version of osCR.c
    open(r"build\osCR.exe")
except:
    # if the compiled version of osCR.c was not found this code will run down bellow
    print(f"{FileManager}: Creating File System")
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