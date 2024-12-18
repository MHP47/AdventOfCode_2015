from utils import *


def part_1(p_Input: str):
    pairings = dict()
    for arrangement in p_Input.strip().splitlines():
        person_a, *_, person_b = arrangement.split()
        person_b = person_b[:-1]
        happiness = next(iter(parse_ints(arrangement))) or 0
        happiness *= 1 if 'gain' in arrangement else -1
        pairings[(person_a, person_b)] = happiness

    return max(
        sum(
            pairings[(a,b)] + pairings[(b,a)]
            for a,b in zip(seating, seating[1:] + (seating[0],))
        )
        for seating in itertools.permutations({x for p in pairings for x in p})
    )


def part_2(p_Input: str):
    pairings = dict()
    for arrangement in p_Input.strip().splitlines():
        person_a, *_, person_b = arrangement.split()
        person_b = person_b[:-1]
        happiness = next(iter(parse_ints(arrangement))) or 0
        happiness *= 1 if 'gain' in arrangement else -1
        pairings[(person_a, person_b)] = happiness

    for person in {x for p in pairings for x in p}:
        pairings[(person, 'self')] = 0
        pairings[('self', person)] = 0

    return max(
        sum(
            pairings[(a,b)] + pairings[(b,a)]
            for a,b in zip(seating, seating[1:] + (seating[0],))
        )
        for seating in itertools.permutations({x for p in pairings for x in p})
    )


example_input_1 = """Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.
"""
challenge_input = Input('13')

assert(part_1(example_input_1) == 330)
print(f"Part 1: {part_1(challenge_input)}")

# assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
