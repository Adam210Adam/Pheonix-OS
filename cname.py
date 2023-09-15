print("Requirements:\nMust Be 4 Characters")
name = input("New Account Name: ")

if len(name) != 4:
    exit()
else:
    open("name.dat", "w").write(name)
    