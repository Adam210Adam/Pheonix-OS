def boot():
    import BooterDir.ROM as ROM

    information = [ROM.loce, ROM.exam]
    infoNumber = 0
    for info in information:
        infoNumber += 1
        print(f"info{infoNumber}{info.name}: {info.value}")