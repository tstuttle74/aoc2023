import math as m
import re


def main():

    # not my solution
    # hat tip reddit user 4HbQ and https://www.reddit.com/r/adventofcode/comments/189m3qw/comment/kbs9g3g
    board = list(open('inputs/day3-input.txt'))
    chars = {(r, c): [] for r in range(140) for c in range(140)
             if board[r][c] not in '01234566789.'}

    for r, row in enumerate(board):
        for n in re.finditer(r'\d+', row):
            edge = {(r, c) for r in (r - 1, r, r + 1)
                    for c in range(n.start() - 1, n.end() + 1)}

            for o in edge & chars.keys():
                chars[o].append(int(n.group()))

    # part 1
    print(sum(sum(p) for p in chars.values()))
    # part 2
    print(sum(m.prod(p) for p in chars.values() if len(p) == 2))


if __name__ == '__main__':
    main()
