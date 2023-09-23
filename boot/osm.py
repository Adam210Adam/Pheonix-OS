class OS_Permission:
          def initws(self, permission):
               if permission == "TrustedInstaller":
                    print("High-Level Security Permission detected\n")
                    password = input("Password: ")
                    password.strip()
                    if password == "987eof":
                         return 3
               elif permission == "Adminstator":
                    return 2
               elif permission == "User":
                    return 1
          

     # Welcome To the OS Manager
class PropertyOS:
          def __init__(self, cmos="NF", name="NF", device="NF") -> None:
               self.cmos = cmos
               self.name = name
               self.device = device
def os():
    try:
     Property = PropertyOS(cmos="UEFI", name="D00STEP-73", device="Dell")
     if PropertyOS(cmos="UEFI", name="D00STEP-73", device="Dell").cmos == "NF":
          raise Exception()
     elif PropertyOS(cmos="UEFI", name="D00STEP-73", device="Dell").device == "NF":
          raise Exception()
     elif PropertyOS(cmos="UEFI", name="D00STEP-73", device="Dell").name == "NF":
          raise Exception()
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
          print(FileManager, end="")
          print(": Creating File System")
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
     print(f"{Cfile.capitalize()}: Successfully loaded C file")
     print(f"{PythonFile.capitalize()}: Executing {Cfile}...")
     BooterDir.boot.boot()
     RunC_code()
    except Exception as err:
          import HLPS.bsod_critical as bsod_critical

          if PropertyOS(cmos="UEFI", name="D00STEP-73", device="Dell").cmos == "NF":
               bsod_critical.bsod(bsod_critical.UNKNOWN_CMOS_BATTERY)
          elif PropertyOS(cmos="UEFI", name="D00STEP-73", device="Dell").device == "NF":
               bsod_critical.bsod(bsod_critical.UNKNOWN_DEVICE)
          elif PropertyOS(cmos="UEFI", name="D00STEP-73", device="Dell").name == "NF":
               bsod_critical.bsod(bsod_critical.UNKNOWN_DEVICE_NAME)
          else:
               bsod_critical.bsod(bsod_critical.INVALID_CALCULATION)