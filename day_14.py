from utils import *


def part_1(p_Input: str, seconds = 2503):
    reindeer = {
        r.split()[0]: parse_ints(r)
        for r in p_Input.strip().splitlines()
    }

    return max(
        (s*t)*(seconds//(t+r)) + (s*t)*min(1,(seconds%(t+r))/t)
        for n,(s,t,r) in reindeer.items()
    )


def part_2(p_Input: str, seconds = 2503):
    reindeer = {
        r.split()[0]: parse_ints(r)
        for r in p_Input.strip().splitlines()
    }

    winner = [
        max(
            (
                (s*t)*(i//(t+r)) + (s*t)*min(1,(i%(t+r))/t),
                n
            )
            for n,(s,t,r) in reindeer.items()
        )[1]
        for i in range(seconds)
    ]

    return Counter(winner).most_common(1)[0][1] - 1


example_input_1 = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
"""
challenge_input = Input('14')

assert(part_1(example_input_1, 1000) == 1120)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1, 1000) == 689)
print(f"Part 2: {part_2(challenge_input)}")
