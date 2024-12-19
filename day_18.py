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


def part_2(p_Input: str, steps = 100):
    lights = Grid(rows=p_Input.strip().splitlines())
    lights.update({
        (0, 0): '#',
        (lights.width - 1, 0): '#',
        (0, lights.height - 1): '#',
        (lights.width - 1, lights.height - 1): '#'
    })

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
        lights.update({
            (0, 0): '#',
            (lights.width - 1, 0): '#',
            (0, lights.height - 1): '#',
            (lights.width - 1, lights.height - 1): '#'
        })

    return len(lights.get_coords_for_value('#'))


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

assert(part_2(example_input_1, 5) == 17)
print(f"Part 2: {part_2(challenge_input)}")
