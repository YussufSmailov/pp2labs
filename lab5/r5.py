import re
text=input()
pat=r'a.+b'
res=re.findall(pat, text)
for r in res:
    print(r)