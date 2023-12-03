import re
import sys


def parse_inputs(file):
    print(f'loading {file}')
    res = []
    with open(file, 'r') as f:
        lines = f.readlines()
        print(f'loaded {len(lines)} lines')
        for line in lines:
            res.append(line.strip())
    return res


# given index into string, find all adjacent numbers and return as int
def find_number(i, line):
    # find start of number
    try:
        start = i
        while start >= 0 and re.match(r'\d', line[start]):
            start -= 1
        start += 1
        # find end of number
        end = i
        while end < len(line) and re.match(r'\d', line[end]):
            end += 1
        end -= 1
        # return number
        num_str = line[start:end + 1]
        return int(num_str)
    except Exception as e:
        raise e


def main():
    # load file and parse lines
    lines = parse_inputs(sys.argv[1])
    # part 1
    # find all numbers
    numbers = set()
    for line in lines:
        for num in re.findall(r'\d+', line):
            numbers.add(int(num))
    # find coordinates of each symbol
    symbols = []
    for i, _ in enumerate(lines):
        for j, _ in enumerate(lines[i]):
            # if symbol (i.e. not a number or literal .) add to list
            if re.match(r'[^\d.]', lines[i][j]):
                # print(f'found symbol {lines[i][j]}')
                symbols.append((i, j))
    # find adjacent numbers to each symbol
    adjacent = set()
    for i, j in symbols:
        # find all numbers adjacent to symbol
        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                # skip if out of bounds
                if x < 0 or y < 0 or x >= len(lines) or y >= len(lines[x]):
                    continue
                # if digit, find all adjacent digits and add to list
                if re.match(r'\d', lines[x][y]):
                    number = find_number(y, lines[x])
                    # print(f'found number {number}')
                    adjacent.add(number)
    # find all numbers not adjacent to any symbol
    result = numbers - adjacent
    print('not adjacent',   result)
    # print result
    print(f'first guess, too low: 330744')
    print(f'num of adjacent: {len(adjacent)}')
    print(f'adjacent sum: {sum(adjacent)}')
    # print(f"adjacent: {adjacent}")



if __name__ == '__main__':
    main()
