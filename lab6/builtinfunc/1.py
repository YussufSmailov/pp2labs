from functools import reduce
n=int(input())
arr=[]
for i in range(n):
    a=int(input())
    arr.append(a)
a=reduce(lambda x,y: x*y, arr)
print(a)