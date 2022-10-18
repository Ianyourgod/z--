import zmm

interpret = zmm.Interpreter()
while True:
    txt = input("Z-- >>> ")
    if txt == "EXIT()":
        break
    interpret.run(txt)