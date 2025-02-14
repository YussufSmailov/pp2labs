
def mygen(start, stop):
    for i in range(start, stop):
        yield i**2

gen=mygen(2, 12)
for num in gen:
    print(num)