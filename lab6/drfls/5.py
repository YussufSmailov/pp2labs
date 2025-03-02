file_name="text.txt"
with open(file_name, "w") as file:
    file.write('[1, 2, 3, 4]')

arr=[1, 2, 4]
file_name="t.txt"
with open(file_name, "w") as file:
    for i in arr:
      file.write(str(i))