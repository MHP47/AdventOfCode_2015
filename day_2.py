from utils import *


def part_1(p_Input):
    presents = [parse_ints(x) for x in p_Input.strip().splitlines()]
    total = 0
    for l,w,h in presents:
        sides = [mul_reduce(x) for x in itertools.combinations((l,w,h), 2)]
        total += 2*sum(sides) + min(sides)
    return total


def part_2(p_Input):
    pass


example_input_1 = """2x3x4
"""
example_input_2 = """1x1x10
"""
challenge_input = Input('2')

assert(part_1(example_input_1) == 58)
assert(part_1(example_input_2) == 43)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
