#Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re
sen=input()
pat=r'[\s,\.]+'
ch=re.sub(pat,':', sen)
print(ch)