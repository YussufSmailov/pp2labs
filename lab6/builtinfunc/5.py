n = int(input())
arr = []

for i in range(n):
    a = input()
    arr.append(a)

tup = tuple(arr)


if all(item not in ["0", "False", "", "None"] for item in tup):
    print("OK")
else:
    print("NO")


t=(1, 0, 3, 4)
s=(False, "hello", 4)
e=("", "jou", "merci")
b=(None, 2, 1, 5)
q=("hello", "you", 2, 4)
print(all(t))
print(all(s))
print(all(e))
print(all(b))
print(all(q))