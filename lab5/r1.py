import re
text=input()
pat=r'ab*'
res=re.findall(pat, text)
if len(res)==0:
    print("Nothing mathced")
else:
    for r in res:
        print(r)
