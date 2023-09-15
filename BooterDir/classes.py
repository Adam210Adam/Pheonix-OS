class Byte:
    def __init__(self, name, value) -> None:
        self.name = name
        self.value = value
class RestorePoint:
    def __init__(self, name) -> None:
        self.name = name
        import BooterDir.ROM as ROM
        ROM.addmemoryRestorePoint(f'{hex(60)}', name)

def TravelToRestorePoint(RestorePoint: RestorePoint):
    with open(f"{RestorePoint.name}.rp", 'r') as openedRestorePoint:
        read = openedRestorePoint.readlines()[0]
        if read == hex(60):
            pass