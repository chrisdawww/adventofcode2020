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
    directions = [[1,0], [1,1], [0,1], [-1,1], [-1,0], [-1,-1], [0,-1], [1, -1]]
    for direction in directions:
        temp_i, temp_j = i, j
        while True:
            temp_i += direction[1]
            temp_j += direction[0]
            if temp_i<0 or temp_j<0 or temp_i>=len(seats) or temp_j>=len(seats[0]):
                break
            if seats[temp_i][temp_j] == '#':
                occupied += 1
                break
            if seats[temp_i][temp_j] == 'L':
                break

    return occupied


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        seats = [[c for c in l.strip()] for l in f.readlines()]

    print(part2(seats))
