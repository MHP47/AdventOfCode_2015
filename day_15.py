from utils import *


def part_1(p_Input: str):
    ingredients = {
        item.split(':')[0]: parse_ints(item)
        for item in p_Input.strip().splitlines()
    }

    def teaspoons_distributions():
        for w in range(0, 101):
            for x in range(0, 101 - w):
                for y in range(0, 101 - w - x):
                    z = 100 - w - x - y
                    yield (w, x, y, z)

    c,d,f,t,_ = zip(*ingredients.values())
    return max(
        mul_reduce(
            max(0, sum([a*b for a,b in zip(dist,q)]))
            for q in (c,d,f,t)
        )
        for dist in teaspoons_distributions()
    )


def part_2(p_Input: str):
    ingredients = {
        item.split(':')[0]: parse_ints(item)
        for item in p_Input.strip().splitlines()
    }

    def teaspoons_distributions():
        for w in range(0, 101):
            for x in range(0, 101 - w):
                for y in range(0, 101 - w - x):
                    z = 100 - w - x - y
                    yield (w, x, y, z)

    c,d,f,t,l = zip(*ingredients.values())
    return max(
        mul_reduce(
            max(0, sum([a*b for a,b in zip(dist,q)]))
            for q in (c,d,f,t)
        )
        for dist in teaspoons_distributions()
        if sum([a*b for a,b in zip(dist,l)]) == 500
    )


example_input_1 = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
"""
challenge_input = Input('15')

# assert(part_1(example_input_1) == 62842880)
print(f"Part 1: {part_1(challenge_input)}")

# assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
