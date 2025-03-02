import os
name="smth.txt"
info=""
with open(name, 'r', encoding="UTF-8") as file:
    info=file.read()

n="new.txt"
with open(n, 'w', encoding="UTF-8") as file:
    file.write(info)