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

direction_coor_deltas = {
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

def char_at(xy: Tuple[int, int], direction: str) -> Tuple[str, Tuple[int, int]]:
    x, y = xy
    dx, dy = direction_coor_deltas[direction]
    x_dx = x + dx
    y_dy = y + dy
    return (grid[x_dx][y_dy], (x_dx, y_dy)) if 0 <= x_dx < len(grid) and 0 <= y_dy < len(grid[x]) else (None, None)

def find_next(cur_xy, prior_xy) -> (Tuple[int, int], str):
    cur_char = grid[cur_xy[0]][cur_xy[1]]
    for test_dir in valid_directions[cur_char]:
        char, coor = char_at(cur_xy, test_dir)
        if char in valid_steps[test_dir] and coor != prior_xy:
            return coor, char
    raise Exception(f"no next step from {cur_xy}")

prior = None
cur = entrance
steps = []
while cur != entrance or prior is None:
    tmp, _ = find_next(cur, prior)
    prior = cur
    cur = tmp
    steps.append(cur)

print(f"correct max steps: 6846")
print(f"max steps: {floor(len(steps)/2)}")
