def palin(s):
    n=s
    b=s[::-1]
    if b==n:
        return "True"
    else:
        return "False"
s=input("enter a string ")
print(palin(s))