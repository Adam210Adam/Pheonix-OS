from time import sleep as wait
from os import system as execute
main_file=open("linker.vsl", "r")
class CompilationError(SyntaxError):
      pass
ps = main_file.readlines()
vsl_STARTED = False
LIB = []
if ps[0] == "vsl_START" or ps[0] == r"vsl_START\n" or ps[0] == "vsl_START\n":
        print("STARTING VSL SESSION >>>")
        vsl_STARTED = True
for line in ps:
    if vsl_STARTED:
        dict2 = {}
        if line=="link" or line == r"link\n" or line == "link\n":
                print("SUCCESS: SETTING MODE TO LINKING >>>")
        elif line=="@IMDTF zcal.apod" or line == r"@IMDTF zcal.apod\n" or line == "@IMDTF zcal.apod\n":
             
             dict2["name"] = "zcal.apod"
             LinesRead = []
             for file in open("zcal.apod").readlines():
                  LinesRead.append(file)
             
             dict2["code"] = LinesRead
        elif dict2 in LIB and line=="run@IMDTF zcal.apod" or line == r"run@IMDTF zcal.apod\n" or line == "run@IMDTF zcal.apod\n":
            execute("python apodC.py zcal.apod")
        elif dict2 not in LIB and line=="run@IMDTF zcal.apod" or line == r"run@IMDTF zcal.apod\n" or line == "run@IMDTF zcal.apod\n":
            raise CompilationError("ZCAL lib unknown")
        elif line=="vsl_END":
                print("ENDING VSL COMPILATION SESSION")
                vsl_STARTED = False
        elif line=="vsl_SLEEP_S1" or line==r"vsl_SLEEP_S1\n" or line=="vsl_SLEEP_S1\n":
            wait(1)
        elif line=="vsl_SLEEP_S2" or line==r"vsl_SLEEP_S2\n" or line=="vsl_SLEEP_S2\n":
            wait(2)
        elif line=="vsl_SLEEP_S3" or line==r"vsl_SLEEP_S3\n" or line=="vsl_SLEEP_S3\n":
            wait(3)
        elif vsl_STARTED == False:
            raise CompilationError("Ended The vsl session then executed code (EXIT CODE 97)")
    else:
         raise CompilationError("The code did not initialize (EXIT CODE 8)")