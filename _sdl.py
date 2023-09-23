import BooterDir.classes, BooterDir.boot, BooterDir.ROM
import hashlib
clast = BooterDir.classes.Byte("clast", 17.9)
pylast = BooterDir.classes.Byte("pylast", 3.11)
rubylast = BooterDir.classes.Byte("rubylast", 38.9)
vsllast = BooterDir.classes.Byte("vsllast", 0.1)
infos = [clast, pylast, rubylast, vsllast]

for information in infos:
        with open(f"{hashlib.sha1(f'{information.name}'.encode()).hexdigest().capitalize()}.dll", "w") as dll:
            dll.write(f"INFO_s_=: {hashlib.sha1(f'{information.value}'.encode()).hexdigest().capitalize()}")
import vsh