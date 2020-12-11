"""
Day 10
Part 1: Find joltages that are 1-3 more than the previous
Part 2: DP to find total combinations of joltage adapters
"""
import numpy as np

def part1(jolts):
    diffs =[]
    sorted_jolts = sorted(jolts)

    for i in range(1, len(sorted_jolts)):
        diffs.append(sorted_jolts[i] - sorted_jolts[i-1])

    uniq, counts = np.unique(diffs, return_counts=True)
    uniq = list(uniq)
    one_diff = counts[uniq.index(1)]
    three_diff = counts[uniq.index(3)]

    return one_diff * three_diff


def part2(graph):
    """
    Traverse depth-first through the graph to build up solutions to sub-
    problems as we find them. The subproblem in this case is the cumulative
    sum of paths to the leaf.
    """
    solutions = {}
    path = [0]

    while path:
        cur_node = path[-1]
        if is_leaf(graph[cur_node]):
            solutions[cur_node] = 1
            path.pop()
            continue

        child = accumulate_child_solutions(cur_node, graph, solutions)
        if child < 0:
            path.pop()
        else:
            path.append(child)

    return solutions[0]


def accumulate_child_solutions(node, graph, solutions):
    # Return the child if it hasn't been found yet, otherwise find the
    # cumulative solution up to that point
    children = graph[node]
    for child in children:
        if child not in solutions:
            return child

    children_sum = sum([solutions[child] for child in children])
    solutions[node] = children_sum
    return -1

def is_leaf(lst):
    return lst == []

def build_graph(jolts):
    """
    Build a dictionary representation of a graph to use in part 2's DP solution
    """
    graph = {}
    for jolt in jolts:
        # Get list of children
        graph_list = [i for i in range(jolt+1, jolt+4) if i in jolts]
        graph[jolt] = graph_list

    return graph


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        jolts = [int(j.strip()) for j in f.readlines()]

    jolts.insert(0,0) # add outlet's voltage
    jolts.append(max(jolts)+3) # add the device's rating
    print(part1(jolts))

    graph = build_graph(jolts)
    print(part2(graph))
