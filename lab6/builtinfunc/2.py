s=input()

cnt=0

upp=len(list(filter(lambda x: ord('Z')>=ord(x)>=ord('A'), s)))
low=len(list(filter(lambda x: ord('z')>=ord(x)>=ord('a'), s)))
print(f"there are {upp} uppercase letters and {low} lowercase letters")