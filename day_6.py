from utils import *


def part_1(p_Input: str):
    lights = Grid(mapping={(x,y): False for x in range(1000) for y in range(1000)})
    for instruction in p_Input.strip().splitlines():
        sx,sy,ex,ey = parse_ints(instruction)
        for x in range(min(sx,ex),max(sx,ex)+1):
            for y in range(min(sy,ey), max(sy,ey)+1):
                if instruction.startswith('turn on'):
                    lights[(x,y)] = True
                elif instruction.startswith('turn off'):
                    lights[(x,y)] = False
                else:
                    lights[(x,y)] = not lights[(x,y)]
    return len(lights.get_coords_for_value(True))


def part_2(p_Input: str):
    lights = Grid(mapping={(x,y): 0 for x in range(1000) for y in range(1000)})
    for instruction in p_Input.strip().splitlines():
        sx,sy,ex,ey = parse_ints(instruction)
        for x in range(min(sx,ex),max(sx,ex)+1):
            for y in range(min(sy,ey), max(sy,ey)+1):
                if instruction.startswith('turn on'):
                    lights[(x,y)] += 1
                elif instruction.startswith('turn off'):
                    lights[(x,y)] = max(lights[(x,y)] - 1, 0)
                else:
                    lights[(x,y)] += 2
    return sum(lights.values())


example_input_1 = """turn on 0,0 through 999,999
"""
example_input_2 = """toggle 0,0 through 999,0
"""
example_input_3 = """turn off 499,499 through 500,500
"""
challenge_input = Input('6')

assert(part_1(example_input_1) == 1_000_000)
assert(part_1(example_input_2) == 1_000)
assert(part_1(example_input_3) == 0)
print(f"Part 1: {part_1(challenge_input)}")

print(f"Part 2: {part_2(challenge_input)}")
