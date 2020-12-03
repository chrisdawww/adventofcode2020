def find_trees(mountain, over, down):
    trees = 0
    run = 0
    mountain = mountain[::down]
    for line in mountain:
        trees += 0 if line[run%len(line)] == '.' else 1
        run += over

    return trees

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        mountain = [l.strip() for l in f.readlines()]

    trees = 1
    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    for (over,down) in slopes:
        trees *= find_trees(mountain, over, down)

    print(trees)

