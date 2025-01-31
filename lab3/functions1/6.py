def rev(sen):
    arr=sen.split()
    arr.reverse()
    s=""
    for i in arr:
        s+=i
        s+=' '
    s.strip()
    return s


sen=input("enter a sentence ")
print(rev(sen))