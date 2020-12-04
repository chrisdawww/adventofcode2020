import re

def part1(passports):
    """
    this is slightly changed for part 2 to get validated passports
    """
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    valid_passports = []
    for passport in passports:
        passport_valid = True
        for field in fields:
            if not field in passport and field != 'cid':
                passport_valid = False
                break
        if passport_valid:
            valid_passports.append(passport)

    print(len(valid_passports))
    return valid_passports

def part2(passports):
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    passports = part1(passports)
    valid_passports = 0
    for passport in passports:
        passport_valid = True
        items = passport.split()
        for item in items:
            field, value = item.split(':')
            if not validate_field(field, value):
                passport_valid = False
        if passport_valid:
            valid_passports += 1

    print(valid_passports)

def validate_field(field, value):
    validation = {
        'byr': lambda x: (len(x) == 4 and (1920 <= int(x) <= 2002)),
        'iyr': lambda x: (len(x) == 4 and (2010 <= int(x) <= 2020)),
        'eyr': lambda x: (len(x) == 4 and (2020 <= int(x) <= 2030)),
        'hgt': lambda x: validate_height(x),
        'hcl': lambda x: validate_hair(x),
        'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
        'pid': lambda x: validate_pid(x),
        'cid': lambda x: True,
    }
    return validation[field](value) if field in validation else False

def validate_hair(color):
    regex = '^#[0-9a-f]{6}$'
    return bool(re.fullmatch(regex, color))

def validate_pid(pid):
    regex = '^[0-9]{9}$'
    return bool(re.fullmatch(regex, pid))

def validate_height(height):
    regex = '^[0-9]{2,3}(in|cm)$'
    if not re.fullmatch(regex, height): return False
    num = height[:-2]
    if 'cm' in height: return (150 <= int(num) <= 193)
    if 'in' in height: return (59 <= int(num) <= 76)

    return False


if __name__ == "__main__":
    passports = []
    with open('input.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        last = 0
        for i, line in enumerate(lines):
            if not line:
                passports.append(' '.join(lines[last:i]))
                last = i

    part2(passports)
