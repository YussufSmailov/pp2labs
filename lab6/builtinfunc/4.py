import time, math
def long_square(num, nedelay):
    time.sleep(nedelay/1000)
    return math.sqrt(num)

print("Sample input: ")
root = float(input())
ms = float(input())
print(f"Square root of {root} after {ms} miliseconds is {long_square(root, ms)}")