
def solve(numheads: int, numlegs: int):
    rabits = numlegs / 2 - numheads
    chickens = 2 * numheads - numlegs / 2
    print(f"Number of rabits {rabits}, and number of chickens {chickens}")