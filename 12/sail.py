"""
Day 12
Part 1: find taxicab distance of ship after instructions execute
"""
import numpy as np

def part1(instructions):
    # dirs: east, south, west, north -- a circular array
    directions = [[1,0], [0,-1], [-1,0], [0,1]]
    card_idx = ['E', 'S', 'W', 'N']
    # heading is index into directions after / 90 and % 4
    heading = 0
    # position vector
    position = [0,0]

    for inst in instructions:
        direction = directions[heading // 90 % 4]
        action = inst[0]
        val = int(inst[1:])

        if action == 'F':
            move_forward(position, direction, val)
        elif action in 'LR':
            val = -val if action == 'L' else val
            heading += val
        elif action in 'NSEW':
            direction = directions[card_idx.index(action)]
            move_forward(position, direction, val)

    return position

def move_forward(position, direction, val):
    position[0] += direction[0] * val
    position[1] += direction[1] * val


def part2(instructions):
    # dirs: east, south, west, north -- a circular array
    directions = [[1,0], [0,-1], [-1,0], [0,1]]
    card_idx = ['E', 'S', 'W', 'N']
    # heading is index into directions after / 90 and % 4
    heading = 0
    # position vector
    position = [0,0]
    waypoint = [10, 1]

    for inst in instructions:
        action = inst[0]
        val = int(inst[1:])

        if action == 'F':
            move_to_waypoint(waypoint, position, val)
        elif action in 'LR':
            val = val if action == 'L' else -val
            waypoint = rotate_waypoint(waypoint, val)
        elif action in 'NSEW':
            direction = directions[card_idx.index(action)]
            move_forward(waypoint, direction, val)

    return position

def rotate_waypoint(waypoint, val):
    rad = np.radians(val)
    cos, sin = np.cos(rad), np.sin(rad)
    rot = np.array([[cos, -sin], [sin, cos]])
    return [round(l) for l in list(np.dot(rot, waypoint))]

def move_to_waypoint(waypoint, position, val):
    position[0] += waypoint[0] * val
    position[1] += waypoint[1] * val

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        instructions = [l.strip() for l in f.readlines()]

    print(part1(instructions))
    print(sum([abs(v) for v in part1(instructions)]))

    print(part2(instructions))
    print(sum([abs(v) for v in part2(instructions)]))
