from utils import *
import json


def part_1(p_Input: str):
    return sum(
        sum(
            parse_ints(x)
        )
        for x in p_Input.strip().splitlines()
    )


def part_2(p_Input: str):
    data = json.loads(p_Input.strip())

    def parse(obj):
        if isinstance(obj, list):
            return sum(
                parse(x)
                for x in obj
            )
        elif isinstance(obj, dict):
            if any('red' == x for x in obj.values()):
                return 0
            return sum(
                parse(x)
                for x in obj.values()
            )
        elif isinstance(obj, str):
            return sum(parse_ints(obj))
        elif isinstance(obj, int):
            return obj
        else:
            raise ValueError(f'Unknown data type {type(obj)} - {obj}')

    return parse(data)


example_input_1 = "[1,2,3]"
example_input_2 = '{"a":2,"b":4}'
example_input_3 = "[[[3]]]"
example_input_4 = '{"a":{"b":4},"c":-1}'
example_input_5 = '{"a":[-1,1]}'
example_input_6 = '[-1,{"a":1}]'
example_input_7 = "[]"
example_input_8 = "{}"
example_input_9 = '[1,{"c":"red","b":2},3]'
example_input_10 = '{"d":"red","e":[1,2,3,4],"f":5}'
example_input_11 = '[1,"red",5]'
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

assert(part_2(example_input_1) == 6)
assert(part_2(example_input_9) == 4)
assert(part_2(example_input_10) == 0)
assert(part_2(example_input_11) == 6)
print(f"Part 2: {part_2(challenge_input)}")
