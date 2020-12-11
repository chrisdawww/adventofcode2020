"""
Day 11
"""

import itertools
import copy

def part1(seats):
    seats_changed = -1
    while seats_changed != 0:
        seats_changed = 0

        temp_changes = copy.deepcopy(seats)
        for i in range(len(seats)):
            for j in range(len(seats[i])):
                num_adjacent = adjacents_occupied(i, j, seats)
                is_occupied = seat_occupied(i, j, seats)

                # skip the floor
                if seats[i][j] == '.':
                    continue

                if num_adjacent == 0 and not is_occupied:
                    temp_changes[i][j] = '#'
                    seats_changed += 1
                elif is_occupied and num_adjacent >= 4:
                    temp_changes[i][j] = 'L'
                    seats_changed += 1
        seats = temp_changes

    return sum([''.join(row).count('#') for row in seats])

def seat_occupied(i, j, seats):
    return seats[i][j] == '#'

def adjacents_occupied(i, j, seats):
    occupied = 0
    for x,y in itertools.product([i-1,i,i+1], [j-1,j,j+1]):
        if x<0 or y<0 or x>len(seats)-1 or y>len(seats[0])-1 or (x==i and y==j):
            continue
        if seats[x][y] == '#':
            occupied += 1
    return occupied

def part2(seats):
    seats_changed = -1
    a = 0
    while seats_changed != 0:
        seats_changed = 0

        temp_changes = copy.deepcopy(seats)
        for i in range(len(seats)):
            for j in range(len(seats[i])):
                # skip the floor
                if seats[i][j] == '.':
                    continue

                num_visible = visible_occupied(i, j, seats)
                is_occupied = seat_occupied(i, j, seats)

                if num_visible == 0 and not is_occupied:
                    temp_changes[i][j] = '#'
                    seats_changed += 1
                elif is_occupied and num_visible >= 5:
                    temp_changes[i][j] = 'L'
                    seats_changed += 1
        seats = temp_changes

    return sum([''.join(row).count('#') for row in seats])

def visible_occupied(i, j, seats):
    occupied = 0
    # check up
    for y in range(i-1, -1, -1):
        if seats[y][j] == '#':
            occupied += 1
            break
        if seats[y][j] == 'L':
            break
    # check down
    for y in range(i+1, len(seats)):
        if seats[y][j] == '#':
            occupied += 1
            break
        if seats[y][j] == 'L':
            break
    # check left
    for x in range(j-1, -1, -1):
        if seats[i][x] == '#':
            occupied += 1
            break
        if seats[i][x] == 'L':
            break
    # check right
    for x in range(j+1, len(seats[0])):
        if seats[i][x] == '#':
            occupied += 1
            break
        if seats[i][x] == 'L':
            break

    # check diag up right
    pairs = [(i-d,j+d) for d in range(min(i+1, len(seats[0])-j))]
    if (i,j) in pairs:
        del pairs[pairs.index((i,j))]
    for x,y in pairs:
        if seats[x][y] == '#':
            occupied += 1
            break
        if seats[x][y] == 'L':
            break
    # check diag up left
    pairs = [(i-d,j-d) for d in range(min(i+1, j+1))]
    if (i,j) in pairs:
        del pairs[pairs.index((i,j))]
    for x,y in pairs:
        if seats[x][y] == '#':
            occupied += 1
            break
        if seats[x][y] == 'L':
            break
    # check diag down right
    pairs = [(i+d,j+d) for d in range(min(len(seats)-i, len(seats[0])-j))]
    if (i,j) in pairs:
        del pairs[pairs.index((i,j))]
    for x,y in pairs:
        if seats[x][y] == '#':
            occupied += 1
            break
        if seats[x][y] == 'L':
            break
    # check diag down left
    pairs = [(i+d,j-d) for d in range(min(len(seats)-i, j+1))]
    if (i,j) in pairs:
        del pairs[pairs.index((i,j))]
    for x,y in pairs:
        if seats[x][y] == '#':
            occupied += 1
            break
        if seats[x][y] == 'L':
            break

    return occupied


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        seats = [[c for c in l.strip()] for l in f.readlines()]

    print(part2(seats))
