# given input number and map, find the output number
import sys


def map_num(src_num, map):
    for i in range(len(map)):
        dest_start, src_start, src_len = map[i]
        offset = src_num - src_start
        if 0 <= offset < src_len:
            return dest_start + offset
    return src_num


def map_all(src_num, maps):
    for i in range(len(maps)):
        src_num = map_num(src_num, maps[i])
    return src_num


lines = list(open('inputs/day5-input.txt'))
#lines = list(open('day5-input-sample.txt'))
seeds = []
maps = []
current_map_idx = -1
for line in lines:
    if line.startswith('seeds:'):
        for num in line.split(':')[1].split():
            seeds.append(int(num))
    elif 'map:' in line:
        current_map_idx+= 1
        maps.append([])
    else:
        nums = line.split()
        if len(nums) > 0:
            maps[current_map_idx].append([int(num) for num in nums])

#locations = [(seed, map_all(seed, maps)) for seed in seeds]
# part 1
#print('min location:', min(locations, key=lambda x: x[1])[1])
# part 2
# group seeds into 2-tuples
seed_ranges = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds) - 1, 2)]
print('seed ranges:', seed_ranges)
print('# seed ranges:', len(seed_ranges))
print('# seeds:', len(seeds))
min_loc = sys.maxsize
seed_range1 = seed_ranges[0]
cnt = 0
# seed_range1 min location: 522761994
start = seed_range1[0]
end = seed_range1[0] + seed_range1[1]
print('start:', start, 'end:', end, 'diff:', end - start)
for s in range(start, end):
    cnt += 1
    if cnt % 1000000 == 0:
        print('cnt:', cnt)
    loc = map_all(s, maps)
    if loc < min_loc:
        min_loc = loc
print('min location:', min_loc)
