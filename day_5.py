from utils import *


def part_1(p_Input: str):
    total = 0
    for word in p_Input.strip().splitlines():
        if any(
            x in word
            for x in ('ab', 'cd', 'pq', 'xy')
        ):
            continue
        if sum([word.count(x) for x in 'aeiou']) < 3:
            continue
        if not re.search(r'(.)\1', word):
            continue
        total += 1
    return total


def part_2(p_Input: str):
    pass


example_input_1 = "ugknbfddgicrmopn"
example_input_2 = "aaa"
example_input_3 = "jchzalrnumimnmhp"
example_input_4 = "haegwjzuvuyypxyu"
example_input_5 = "dvszwmarrgswjxmb"
challenge_input = Input('5')

assert(part_1(example_input_1) == 1)
assert(part_1(example_input_2) == 1)
assert(part_1(example_input_3) == 0)
assert(part_1(example_input_4) == 0)
assert(part_1(example_input_5) == 0)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
