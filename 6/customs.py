def part1(lines):
    groups = []

    cur_group = []
    for line in lines:
        cur_group.extend(line)
        if not line or line == lines[-1]:
            groups.append(len(set(cur_group)))
            cur_group = []
            continue

    return sum(groups)

def part2(lines):
    groups = []

    cur_group = []
    for line in lines:
        if line:
            cur_group.append({l for l in line})
        if not line or line == lines[-1]:
            groups.append(len(set.intersection(*cur_group)))
            cur_group = []
            continue

    return sum(groups)


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]

    print(part2(lines))
