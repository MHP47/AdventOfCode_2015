from utils import *
from sympy import divisors


def part_1(p_Input: str):
    goal = int(p_Input)
    low = 1
    high = 1_000_000

    while low <= high:
        mid = (low + high) // 2
        if sum(x*10 for x in divisors(mid)) >= goal:
            high = mid - 1
        else:
            low = mid + 1

    return min(
        value
        for value in range(1, high)
        if sum(x*10 for x in divisors(value)) >= goal
    )


def part_2(p_Input: str):
    pass


challenge_input = '29000000'

print(f"Part 1: {part_1(challenge_input)}")

print(f"Part 2: {part_2(challenge_input)}")
