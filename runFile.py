import zmm
from sys import argv

f = open(argv[1],"r")
fcont = f.read()
f.close()

lines = []
line = ""
for i in fcont:
    if i == "\n":
        lines.append(line)
        line = ""
    else:
        line += i
lines.append(line)
interpreter = zmm.Interpreter()
ln = 0
for i in lines:
    ln += 1
    interpreter.run(i,ln)
