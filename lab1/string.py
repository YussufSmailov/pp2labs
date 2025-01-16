print("Hello")
print('Hello')

#You can use quotes inside a string, as long as they don't match the quotes surrounding the string:

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')


#Assign String to a Variable
a = "Hello"
print(a)

#Multiline Strings
#You can assign a multiline string to a variable by using three quotes
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


#Or three single quotes:
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)


a = "Hello, World!"
print(a[1])

for x in "banana":
  print(x)


a = "Hello, World!"
print(len(a))


txt = "The best things in life are free!"
print("free" in txt)


txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")