"""
Day 9
XMAS "encryption"
Part 1: Find the first number where there aren't two numbers in the previous
25 which sum to it
Part 2: Find a contiguous set of numbers which add to the target found from
the first part
"""

def part1(nums):
    for i in range(len(nums)):
        preamble = nums[i:i+25]
        target = nums[i+25]

        if not check_preamble(target, preamble):
            return target

    return -1

def check_preamble(target, preamble):
    for i, num in enumerate(preamble):
        need = target - num
        if need in preamble:
            return i, preamble.index(need)

    return False

def part2(target, nums):
    # Start at the beginning of the array, then from 2, work our way up until
    # we're at or over the target
    for i, start_num in enumerate(nums):
        for length in range(2, len(nums)-i-1):
            contig_set = nums[i:i+length]
            contig_sum = sum(contig_set)

            if contig_sum == target:
                return sum([min(contig_set), max(contig_set)])

            if contig_sum > target:
                break

    return -1



if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        numbers = [int(l.strip()) for l in f.readlines()]

    #ans = part1(numbers)

    target = 85848519
    print(part2(target, numbers))
