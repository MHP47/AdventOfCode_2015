from utils import *
import networkx as nx


def part_1(p_Input: str):
    routes = {}
    for route in p_Input.strip().splitlines():
        locs, dist = route.split(' = ')
        loc_a, loc_b = locs.split(' to ')
        dist = int(dist)
        routes[(loc_a, loc_b)] = dist
        routes[(loc_b, loc_a)] = dist

    locations = {x for tup in routes for x in tup}
    graph = nx.Graph(list(routes))
    graph.add_nodes_from(locations)

    return min(
        sum(routes[k] for k in zip(path, path[1:]))
        for start, end in itertools.permutations(locations, 2)
        for path in nx.all_simple_paths(graph, source=start, target=end)
        if len(path) == len(locations)
    )


def part_2(p_Input: str):
    routes = {}
    for route in p_Input.strip().splitlines():
        locs, dist = route.split(' = ')
        loc_a, loc_b = locs.split(' to ')
        dist = int(dist)
        routes[(loc_a, loc_b)] = dist
        routes[(loc_b, loc_a)] = dist

    locations = {x for tup in routes for x in tup}
    graph = nx.Graph(list(routes))
    graph.add_nodes_from(locations)

    return max(
        sum(routes[k] for k in zip(path, path[1:]))
        for start, end in itertools.permutations(locations, 2)
        for path in nx.all_simple_paths(graph, source=start, target=end)
        if len(path) == len(locations)
    )


example_input_1 = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
"""
challenge_input = Input('9')

assert(part_1(example_input_1) == 605)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == 982)
print(f"Part 2: {part_2(challenge_input)}")
