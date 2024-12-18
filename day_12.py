from utils import *


def part_1(p_Input: str):
    return sum(
        sum(
            parse_ints(x)
        )
        for x in p_Input.strip().splitlines()
    )


def part_2(p_Input: str):
    pass


example_input_1 = "[1,2,3]"
example_input_2 = '{"a":2,"b":4}'
example_input_3 = "[[[3]]]"
example_input_4 = '{"a":{"b":4},"c":-1}'
example_input_5 = '{"a":[-1,1]}'
example_input_6 = '[-1,{"a":1}]'
example_input_7 = "[]"
example_input_8 = "{}"
challenge_input = Input('12')

assert(part_1(example_input_1) == 6)
assert(part_1(example_input_2) == 6)
assert(part_1(example_input_3) == 3)
assert(part_1(example_input_4) == 3)
assert(part_1(example_input_5) == 0)
assert(part_1(example_input_6) == 0)
assert(part_1(example_input_7) == 0)
assert(part_1(example_input_8) == 0)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
