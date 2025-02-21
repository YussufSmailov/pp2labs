import re
text=input()
pat=r'ab*'
res=re.search(pat, text)
for r in res:
    print(r)
