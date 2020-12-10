"""
Day 8
"Boot code" instructions
acc +n: increase the accumulator value by n
jmp +-n: jump + or - n instructions
nop +-n: continue to the next operation
"""
import copy

def parse_instructions(instructions):
    """
    Read every instruction and get a tuple of the following format:
        [instruction string, int value, visited boolean]
    """
    inst_list = []
    for instruction in instructions:
        inst, val = instruction.split()
        val = int(val)
        inst_list.append([inst, val, False])

    return inst_list


def part1(instructions):
    accumulator = 0
    inst_idx = 0
    while inst_idx < len(instructions):
        instruction, value, visited = instructions[inst_idx]
        if visited:
            return accumulator
        instructions[inst_idx][-1] = True

        if 'acc' in instruction:
            accumulator += value
            inst_idx += 1
        elif 'nop' in instruction:
            inst_idx += 1
        elif 'jmp' in instruction:
            inst_idx += value

    return -1


def part2(instructions):
    i = 0
    while i < len(instructions):
        inst, val, visited = instructions[i]
        if inst == 'acc':
            i += 1
            continue
        else:
            new_instructions = copy.deepcopy(instructions)

        if inst == 'jmp':
            new_instructions[i] = ['nop', val, visited]
        elif inst == 'nop':
            new_instructions[i] = ['jmp', val, visited]

        result = test_instructions(new_instructions)
        if result > 0:
            return result
        else:
            i += 1

    return -1

def test_instructions(instructions):
    accumulator = 0
    inst_idx = 0
    while inst_idx < len(instructions):
        instruction, value, visited = instructions[inst_idx]
        if visited:
            return -1
        instructions[inst_idx][-1] = True

        if 'acc' in instruction:
            accumulator += value
            inst_idx += 1
        elif 'nop' in instruction:
            inst_idx += 1
        elif 'jmp' in instruction:
            inst_idx += value

    return accumulator

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        instructions_str = [l.strip() for l in f.readlines()]

    instructions = parse_instructions(instructions_str)

    #print(part1(instructions))
    print(part2(instructions))
