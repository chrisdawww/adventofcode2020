"""
Day 13--doin this before day 12, whoops missed a couple days due to relaxing
after the school quarter ended

Part 1: Determine the earliest bus we can take given busses at regular intervals
"""
import re
import math

def part1(timestamp, busses):
    # Return the bus that repeats next after timestamp (there will only be 1).
    next_busses = [bus * ((timestamp // bus) + 1) for bus in busses]
    soonest = min(next_busses)
    bus_id = busses[next_busses.index(soonest)]
    soonest = soonest - timestamp

    return soonest*bus_id

def part2(busses, bus_idx):
    st, sp = 1,1
    for bus, idx in sorted(list(zip(busses, bus_idx)))[::-1]:
        st, sp = next_loc(st, sp, bus, idx)

    return st

def next_loc(start, step, num, remainder):
    mult = step*num
    for i in range(start, mult, step):
        if not (i+remainder) % num:
            break
    return i, mult



if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]

    timestamp = int(lines[0])
    pattern = re.compile('\d+')
    busses = [int(bus) for bus in lines[1].split(',') if pattern.match(bus)]
    bus_idx = [lines[1].split(',').index(str(bus)) for bus in busses]

    print(part1(timestamp, busses))
    print(part2(busses, bus_idx))

