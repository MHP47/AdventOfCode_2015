from utils import *


def part_1(p_Input: str):
    location = 0j
    visited = set([location])
    for step in p_Input.strip():
        location += {
            '<': -1j,
            '>': 1j,
            '^': -1,
            'v': 1
        }[step]
        visited.add(location)
    return len(visited)


def part_2(p_Input: str):
    santa = 0j
    robot = 0j
    visited = set([santa])
    for s,r in chunks(p_Input.strip(), 2):
        santa += {
            '<': -1j,
            '>': 1j,
            '^': -1,
            'v': 1
        }[s]
        robot += {
            '<': -1j,
            '>': 1j,
            '^': -1,
            'v': 1
        }[r]
        visited.add(santa)
        visited.add(robot)
    return len(visited)


example_input_1 = ">"
example_input_2 = "^>v<"
example_input_3 = "^v^v^v^v^v"
example_input_4 = "^v"
challenge_input = Input('3')

assert(part_1(example_input_1) == 2)
assert(part_1(example_input_2) == 4)
assert(part_1(example_input_3) == 2)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_4) == 3)
assert(part_2(example_input_2) == 3)
assert(part_2(example_input_3) == 11)
print(f"Part 2: {part_2(challenge_input)}")
