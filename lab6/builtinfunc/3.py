
a=input()
s=list(map(lambda x: str(x), reversed(a)))
e=''.join(s)
print(e)
if a==e:
    print("OK")
else:
    print("NO")