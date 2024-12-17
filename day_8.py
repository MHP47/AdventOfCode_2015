from utils import *


def part_1(p_Input: str):
    return sum(
        len(x) - len(eval(x))
        for x in p_Input.strip().splitlines()
    )


def part_2(p_Input: str):
    pass


example_input_1 = '''""
"abc"
"aaa\\"aaa"
"\\x27"
'''
challenge_input = Input('8')

assert(part_1(example_input_1) == 12)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
