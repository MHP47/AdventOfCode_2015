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
    replacement_mappings, molecule = p_Input.strip().split('\n\n')
    replacements = dict()
    goal = "e"

    for r in replacement_mappings.splitlines():
        k,v = r.split(' => ')
        replacements[v] = k

    def h(s):
        if not s: return BIG
        return iterative_levenshtein(goal, s)

    def m(s):
        for k,v in replacements.items():
            for i,j in [(m.start(), m.end()) for m in re.finditer(k, s)]:
                yield f"{s[:i]}{v}{s[j:]}"

    return len(astar_search(molecule, h, m)) - 1


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
example_input_3 = """e => H
e => O
H => HO
H => OH
O => HH

HOH
"""
example_input_4 = """e => H
e => O
H => HO
H => OH
O => HH

HOHOHO
"""
challenge_input = Input('19')

assert(part_1(example_input_1) == 4)
assert(part_1(example_input_2) == 7)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_3) == 3)
assert(part_2(example_input_4) == 6)
print(f"Part 2: {part_2(challenge_input)}")
