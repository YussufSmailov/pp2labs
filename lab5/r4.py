import re
text=input()
pat=r'[A-Z][a-z]+'
res=re.findall(pat, text)
for r in res:
    print(r)