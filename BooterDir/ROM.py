import BooterDir.classes as classes
loce = classes.Byte("loce", 9848)
exam = classes.Byte("exam", 82)
def addmemoryRestorePoint(address, filename) :
    with open(f"{filename}.rp", "w") as restore_point:
        restore_point.write(f"{address}")