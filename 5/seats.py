import numpy as np

def part1(seats):
    max_seat = 0
    for seat in seats:
        row = bin_space_part(seat[:7])
        col = bin_space_part(seat[7:])
        seat_id = get_id(row, col)

        max_seat = max(max_seat, seat_id)

    return max_seat

def part2(seats):
    all_seats = np.arange(1024)
    found_seats = []
    for seat in seats:
        row = bin_space_part(seat[:7])
        col = bin_space_part(seat[7:])
        found_seats.append(get_id(row, col))
    found_seats = np.array(found_seats)

    missing_seats = np.setdiff1d(all_seats, found_seats)
    for i in range(1,len(missing_seats)-1):
        missing_id = missing_seats[i]
        left = missing_seats[i-1]
        right = missing_seats[i+1]
        if left+1 != missing_id != right-1:
            return missing_id

    return -1

def bin_space_part(enc):
    """
    Binary Space Partition
    A 'B' or an 'R' mean that the current proposal is now over the latter half
    of wherever we are so increase the proposal by half of the space we are
    considering.
    """
    start_idx = 0
    half = 2 ** (len(enc) - 1)
    for char in enc:
        if char in ['B', 'R']:
            start_idx += half
        half //= 2

    return start_idx

def get_id(row, col):
    return row * 8 + col


if __name__ == "__main__":
    with open('input.txt') as f:
        seats = [l.strip() for l in f.readlines()]
    print(part1(seats))
    print(part2(seats))
