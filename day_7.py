from utils import *


def calculate_gate(connection: str, gates: dict):
        if connection.isnumeric():
            return int(connection)
        components = connection.split()
        try:
            _x,v,_y = components
            x = gates.get(_x)
            if x is None: x = int(_x)
            y = gates.get(_y)
            if y is None: y = int(_y)
            return {
                'AND': x & y,
                'RSHIFT': x >> y,
                'OR': x | y,
                'LSHIFT': x << y,
            }[v]
        except ValueError:
            try:
                _,_y = components
                y = gates.get(_y)
                if y is None: y = int(_y)
                return ~y & 0xFFFF
            except ValueError:
                return gates[components[0]]


def part_1(p_Input: str, lookup='a'):
    circuits = {
        k: v
        for x in p_Input.strip().splitlines()
        for v,k in [x.split(' -> ')]
    }
    path = [{(lookup, circuits[lookup])}]
    while True:
        if step := {
            (x,circuits[x])
            for wire, gate in path[-1]
            for x in re.findall(r'[a-z]+', gate)
        }:
            path.append(step)
        else:
            break

    gates = dict()
    
    for i in path[::-1]:
        for wire, signal in i:
            gates[wire] = calculate_gate(signal, gates)

    return gates[lookup]


def part_2(p_Input: str):
    val = part_1(p_Input)
    p_Input = re.sub('\n[0-9]+ -> b', f'\n3176 -> b', p_Input)
    return part_1(p_Input)


example_input_1 = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
"""
challenge_input = Input('7')

assert(part_1(example_input_1, 'x') == 123)
assert(part_1(example_input_1, 'y') == 456)
assert(part_1(example_input_1, 'h') == 65412)
assert(part_1(example_input_1, 'd') == 72)
assert(part_1(example_input_1, 'f') == 492)
assert(part_1(example_input_1, 'e') == 507)
assert(part_1(example_input_1, 'i') == 65079)
assert(part_1(example_input_1, 'g') == 114)
print(f"Part 1: {part_1(challenge_input)}")

# assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
