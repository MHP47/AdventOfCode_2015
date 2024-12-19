from utils import *


def part_1(p_Input: str, litres=150):
    buckets = list(map(int, p_Input.strip().splitlines()))
    total = 0
    for i in itertools.count(1):
        combos = list(itertools.combinations(buckets, i))
        if all(
            sum(x) > litres
            for x in combos
        ):
            break
        total += sum(
            sum(c) == litres
            for c in combos
        )
    return total


def part_2(p_Input: str):
    pass


example_input_1 = """20
15
10
5
5
"""
challenge_input = Input('17')

assert(part_1(example_input_1, 25) == 4)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
