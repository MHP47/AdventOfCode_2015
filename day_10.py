from utils import *


def round(sequence):
    return cat(
        cat(
            map(str,
                (len(list(v)), k)
            )
        )
        for k,v in itertools.groupby(sequence)
    )


def part_1(p_Input: str, iterations=40):
    seq = p_Input
    for _ in range(iterations):
        seq = round(seq)
    return len(seq)


def part_2(p_Input: str):
    pass


example_input_1 = "1"
example_input_2 = "11"
example_input_3 = "21"
example_input_4 = "1211"
example_input_5 = "111221"
challenge_input = '1113222113'

assert(part_1(example_input_1, 1) == 2)
assert(part_1(example_input_2, 1) == 2)
assert(part_1(example_input_3, 1) == 4)
assert(part_1(example_input_4, 1) == 6)
assert(part_1(example_input_5, 1) == 6)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
