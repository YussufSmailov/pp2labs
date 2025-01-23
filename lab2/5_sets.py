myset = {"apple", "banana", "cherry"}

#access set items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#update set items
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#removing elem
thisset = {"apple", "banana", "cherry"}
thisset.discard("orange")
print(thisset)

#join sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)