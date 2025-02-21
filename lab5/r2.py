import re
text=input()
pat=r'ab{2,3}'
res=re.findall(pat, text)
if len(res)==0:
    print("Nothing mathced")
else:
    for r in res:
        print(r)