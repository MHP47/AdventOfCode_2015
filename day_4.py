from utils import *
import hashlib


def part_1(p_Input: str):
    for key in itertools.count(1):
        if hashlib.md5(f"{p_Input}{key}".encode('utf-8')).hexdigest().startswith('00000'):
            return key


def part_2(p_Input: str):
    for key in itertools.count(1):
        if hashlib.md5(f"{p_Input}{key}".encode('utf-8')).hexdigest().startswith('000000'):
            return key


example_input_1 = "abcdef"
example_input_2 = "pqrstuv"
challenge_input = 'iwrupvqb'

assert(part_1(example_input_1) == 609043)
assert(part_1(example_input_2) == 1048970)
print(f"Part 1: {part_1(challenge_input)}")

# assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
