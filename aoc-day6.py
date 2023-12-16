import math

def parse_number_line(s):
    return [int(num) for num in s.split(':')[1].split()]

def ways_to_win(t, d):
    a = -1; b = t; c = -d
    bac = math.sqrt(b ** 2 - 4 * a * c)
    root1 = (-b + bac) / (2 * a)
    root2 = (-b - bac) / (2 * a)
    ceil = math.ceil(root1)
    floor = math.floor(root2)
    lower = ceil if ceil > root1 else ceil + 1
    upper = floor if floor < root2 else floor - 1
    return upper - lower + 1

lines = list(open('inputs/day6-input.txt'))
#lines = list(open('inputs/day6-input-sample.txt'))

time = []
distance = []
for line in lines:
    if line.startswith('Time:'):
        time = parse_number_line(line)
    elif line.startswith('Distance:'):
        distance = parse_number_line(line)

pt_1 = [ways_to_win(t, distance[i]) for i, t in enumerate(time)]
print('part 1', math.prod(pt_1))

total_time = ''.join([str(t) for t in time])
total_dist = ''.join([str(t) for t in distance])
pt_2 = ways_to_win(int(total_time), int(total_dist))
print('part 2', pt_2)