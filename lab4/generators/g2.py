n=int(input())
def mygen(start, stop):
    while(start<stop):
        if start%2==0:
            yield start
        start+=1

# gen=mygen(0, n)
# arr=[]
# for num in gen:
   
#     arr.append(num)
print(*mygen(0, n), sep=", ")