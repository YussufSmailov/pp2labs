import os
path=r"C:\Users\irresible\Desktop\pp2labs\lab6\drfls\1.py"
dir=os.path.dirname(path)
file=os.path.basename(path)
if os.path.exists(path):
    print(f'directory-{dir}, file-{file}')
else:
    print('path doesnt exist')