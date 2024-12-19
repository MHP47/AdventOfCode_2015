from utils import *


def part_1(p_Input: str, steps = 100):
    lights = Grid(rows=p_Input.strip().splitlines())

    for _ in range(steps):
        new = dict()

        for k in lights:
            on_count = sum(
                lights[x] == '#'
                for x in neighbors8(k)
                if x in lights
            )

            if lights[k] == '#':
                new[k] = '#' if on_count in (2,3) else '.'
            else:
                new[k] = '#' if on_count == 3 else '.'

        lights.update(new)

    return len(lights.get_coords_for_value('#'))


def part_2(p_Input: str):
    pass


example_input_1 = """.#.#.#
...##.
#....#
..#...
#.#..#
####..
"""
challenge_input = Input('18')

assert(part_1(example_input_1, 4) == 4)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
