n=int(input())
def mygen(start, stop):
    while(start<stop):
        yield start**2
        start+=1

gen=mygen(0, n)
for num in gen:
    print(num)