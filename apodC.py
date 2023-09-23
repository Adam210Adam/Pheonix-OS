from sys import argv as args

filename = args[1]
class Codes:
    zcal = ["print(\"Welcome to ZCAL\")", "num1=input(\"NUM1: \")", "num2=input(\"NUM2: \")", "print(num1 + num2)"]
if filename == "zcal.apod":
    with open("zcal.apod") as file:
        if file.readlines()[0] == "exec":
            for line in Codes.zcal:
                exec(line)