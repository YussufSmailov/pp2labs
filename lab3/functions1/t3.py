def solve(numheads, numlegs):
    # x+y=35
    # 2*x+4*y=94
    rabbits=(numlegs-numheads*2)/2
    chickens=(numheads*4-numlegs)/2
    print("chickens = ", chickens, "rabbits = ", rabbits)


numheads=35
numlegs=94
solve(numheads, numlegs)
