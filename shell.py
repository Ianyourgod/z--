import zmm

interpret = zmm.Interpreter()
ln = 0
while True:
    ln += 1
    txt = input("Z-- >>> ")
    if txt == "EXIT()":
        break
    interpret.run(txt,ln)