def spy_game(arr):
    s=""
    for i in arr:
        s+=str(i)
    if s.find("007")!=-1:
        return "True"
    else:
        return "False"
n=int(input("length of list "))
arr=[]
for i in range(n):
    q=int(input('enter a num '))
    arr.append(q)
print(spy_game(arr))