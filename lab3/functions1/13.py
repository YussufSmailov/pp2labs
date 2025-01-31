import random as rd
print("Hello! What is your name?")
name=input("")
cnt=0
gs=rd.randint(1, 21)
print(gs)
print(f"Well, {name}, I am thinking of a number between 1 and 20.")
while True:
    print("Take a guess.")
    guess=int(input(""))
    if guess<gs:
        print("Your guess is too low.")
        cnt+=1
        continue
    if guess>gs:
        print("Your guess is too high.")
        cnt+=1
        continue
    else:
        print(f"Good job, {name}! You guessed my number in {cnt} guesses!")
        break

