import os as oss
from boot.osm import *
class Drive:
    def __init__(self, sizeInBytes=512, name="Unamed Volume 1", type="SATA", typeHF="HD", main=False) -> None:
        self.sizeInBytes = sizeInBytes
        self.name = name
        self.type = type
        self.HDFD = typeHF
        self.main = main
        self.running = False
    def run(self, Permission: OS_Permission):
        if Permission == 3:
            modules = ["calendar", "mistune", "sre_constants", "IPython", "certifi", "mmap", "sre_parse", "PIL", "cffi", "mmapfile", "ssl", "PyInstaller", "sspi", "PyQt5"]
            modules2 = ["calendar", "mistune", "sre_constants", "IPython", "certifi", "mmap", "sre_parse", "PIL", "cffi", "mmapfile", "ssl", "PyInstaller", "sspi", "PyQt5"]
            for module in modules:
                oss.system(f"pip install {module}")
                print(f"Installing | {module}")
cdrive = Drive(512, "C", "SATA", "HD", False)
cdrive.run(OS_Permission.initws(self=cdrive, permission="TrustedInstaller"))
os()