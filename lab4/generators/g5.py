n=int(input())
def mygen(start):
    for i in range(start,-1,-1):
        yield i

gen=mygen(n)
for num in gen:
    print(num)