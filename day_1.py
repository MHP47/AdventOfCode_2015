from utils import *


def part_1(p_Input: str):
    return p_Input.count('(') - p_Input.count(')')


def part_2(p_Input):
    floor = 0
    for i,m in enumerate(p_Input, 1):
        floor += {
            '(': 1,
            ')': -1
        }[m]
        if floor == -1:
            return i


example_input_1 = "(())"
example_input_2 = "()()"
example_input_3 = "((("
example_input_4 = "(()(()("
example_input_5 = "))((((("
example_input_6 = "())"
example_input_7 = "))("
example_input_8 = ")))"
example_input_9 = ")())())"
example_input_10 = ")"
example_input_11 = "()())"
challenge_input = Input('1')

assert(part_1(example_input_1) == 0)
assert(part_1(example_input_2) == 0)
assert(part_1(example_input_3) == 3)
assert(part_1(example_input_4) == 3)
assert(part_1(example_input_5) == 3)
assert(part_1(example_input_6) == -1)
assert(part_1(example_input_7) == -1)
assert(part_1(example_input_8) == -3)
assert(part_1(example_input_9) == -3)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_10) == 1)
assert(part_2(example_input_11) == 5)
print(f"Part 2: {part_2(challenge_input)}")
