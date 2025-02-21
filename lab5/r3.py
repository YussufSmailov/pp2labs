import re
text=input()
pat=r'[a-z]+_[a-z]'
res=re.findall(pat, text)
for r in res:
    print(r)