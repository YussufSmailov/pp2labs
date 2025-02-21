import re
s=input()
pat=r'[A-Z]+'
ch=re.split(pat, s)
print(ch)