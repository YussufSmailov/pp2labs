import re
camel = input()
snake= "this_is_camel_case"
p=r'[A-Z]'
l=re.findall(p, camel)
res=re.split(p, camel)
print(l)
print(res)

while "" in res:
    res.remove("")

ans=[]
for i in range(len(res)):
    if i==len(res)-1:
        ans.append(l[i]+res[i])
    else:
        ans.append(l[i]+res[i]+'_')

final=""
for i in ans:
    final+=i
print(final.lower())
