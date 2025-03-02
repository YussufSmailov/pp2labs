import os
path=r"C:\Users\irresible\Desktop\pp2labs\lab6\drfls\asd"

if os.path.exists(path) and os.access(path, os.F_OK):
    os.remove('asd')
    print("deleted")
else:
    print("path doesnt exist")