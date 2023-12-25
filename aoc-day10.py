from math import floor
from typing import List, Tuple


#lines = list(open('inputs/day10-sample.txt'))
lines = list(open('inputs/day10.txt'))

entrance: Tuple[int, int] = (-1, -1)
grid: List[str] = []
for i, line in enumerate(lines):
    if 'S' in line:
        entrance = (i, line.index('S'))
    grid.append(line.strip())

directions = {
    'N': (-1, 0),
    'S': (1, 0),
    'E': (0, 1),
    'W': (0, -1)
}

valid_steps = {
    'N': ['|', '7', 'F', 'S'],
    'S': ['|', 'J', 'L', 'S'],
    'E': ['-', 'J', '7', 'S'],
    'W': ['-', 'F', 'L', 'S'],
}

valid_directions = {
    '|': ['N', 'S'],
    '-': ['E', 'W'],
    '7': ['S', 'W'],
    'J': ['W', 'N'],
    'F': ['S', 'E'],
    'L': ['N', 'E'],
    'S': ['N', 'S', 'E', 'W'],
}

def char_at(coor: Tuple[int, int], dir: str) -> Tuple[str, Tuple[int, int]]:
    x, y = coor
    dx, dy = directions[dir]
    x_dx = x + dx
    y_dy = y + dy
    return (grid[x_dx][y_dy], (x_dx, y_dy)) if 0 <= x_dx < len(grid) and 0 <= y_dy < len(grid[x]) else (None, None)

def find_next(cur_coor, prior_cur) -> (Tuple[int, int], str):
    for test_dir in valid_directions[grid[cur_coor[0]][cur_coor[1]]]:
        char, coor = char_at(cur_coor, test_dir)
        if char in valid_steps[test_dir] and coor != prior_cur:
            return coor, char
    raise Exception(f"no next step from {cur_coor}")

prior_coor = None
cur_coor = entrance
steps = []
while cur_coor != entrance or prior_coor is None:
    tmp, char = find_next(cur_coor, prior_coor)
    prior_coor = cur_coor
    cur_coor = tmp
    steps.append(cur_coor)

print(f"max steps: {floor(len(steps)/2)}")
