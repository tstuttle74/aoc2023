import sys
import re

digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def as_digit(s):
    return digits[s] if s in digits else s


def parse_inputs(file):
    print(f'loading {file}')
    numbers = []
    with open(file, 'r') as f:
        lines = f.readlines()
        print(f'loaded {len(lines)} lines')
        for line in lines:
            trimmed = line.strip()
            # use lookahead assertion (?=...) to find overlapping matches. tricky!
            matches = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', trimmed)
            if len(matches) > 0:
                i = int(as_digit(matches[0]) + as_digit(matches[-1]))
                numbers.append(i)
                #print(f'{trimmed} -> {i}')
            else:
                raise f'ERROR: not enough numbers in line {trimmed}'

    return numbers


if __name__ == '__main__':
    # load file and parse lines
    nums = parse_inputs(sys.argv[1])
    # do stuff
    print('first, too low', 54412)
    print('correct', 54418)
    print('answer', sum(nums))


