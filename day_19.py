from utils import *


def part_1(p_Input: str):
    replacement_mappings, molecule = p_Input.strip().split('\n\n')
    replacements = defaultdict(set)
    medicine = set()

    for r in replacement_mappings.splitlines():
        k,v = r.split(' => ')
        replacements[k].add(v)

    for k,v in replacements.items():
        for n in [m.start() for m in re.finditer(k, molecule)]:
            for c in v:
                if len(k) == 1:
                    medicine.add(f"{molecule[:n]}{c}{molecule[n+1:]}")
                elif len(k) == 2 and molecule[n+1] == k[1]:
                    medicine.add(f"{molecule[:n]}{c}{molecule[n+2:]}")

    return len(medicine)


def part_2(p_Input: str):
    pass


example_input_1 = """H => HO
H => OH
O => HH

HOH
"""
example_input_2 = """H => HO
H => OH
O => HH

HOHOHO
"""
challenge_input = Input('19')

assert(part_1(example_input_1) == 4)
assert(part_1(example_input_2) == 7)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
