import re
text=input()
pat=r'ab{2,3}'
res=re.findall(pat, text)
for r in res:
    print(r)
