from utils import *


def part_1(p_Input: str):
    ticker = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1
"""
    mfcsam = {
        compound.split(':')[0]: parse_ints(compound)[0]
        for compound in ticker.strip().splitlines()
    }

    sues = {}
    for aunt in p_Input.strip().splitlines():
        id = parse_ints(aunt)[0]
        sues[id] = {
            t.replace(':', ''): int(v.replace(',',''))
            for t,v in chunks(aunt.split()[2:], 2)
        }

    for id,q in sues.items():
        if all(mfcsam[k] == v for k,v in q.items()):
            return id


def part_2(p_Input: str):
    pass


challenge_input = Input('16')

print(f"Part 1: {part_1(challenge_input)}")

print(f"Part 2: {part_2(challenge_input)}")
