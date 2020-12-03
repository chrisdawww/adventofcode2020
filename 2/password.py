def main():
    with open('input.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]

    num_valid_pw = 0
    for line in lines:
        min_num, max_num, letter, password = get_pw_reqs(line)

        num_valid_pw += validate_p2(min_num, max_num, letter, password)

    print(num_valid_pw)

def get_pw_reqs(line):
    nums, letter, password = line.split()
    min_num, max_num = nums.split('-')
    letter = letter[0]

    return int(min_num), int(max_num), letter, password

def validate_p2(min_num, max_num, letter, password):
    min_num -= 1
    max_num -= 1

    count = f'{password[min_num]}{password[max_num]}'.count(letter)

    return 0 if count != 1 else 1

def validate_p1(min_num, max_num, letter, password):
    count = password.count(letter)
    if min_num <= count <= max_num:
        return 1
    else:
        return 0


if __name__ == "__main__":
    main()
