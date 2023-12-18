import re

#lines = list(open('inputs/day8-sample2.txt'))
lines = list(open('inputs/day8.txt'))

graph = {}
dirs = None
for line in lines:
    if dirs is None:
        dirs = line.strip()
        continue
    parts = line.split('=')
    if len(parts) == 2:
        key = parts[0].strip()
        [left, right] = re.findall(r'\w+', parts[1])
        graph[key] = (left, right)
π
ptrs = [k for k in graph.keys() if k.endswith('A')]
i = 0
while len([p for p in ptrs if not p.endswith('Z')]) > 0:
    if i % 100000 == 0:
        print(i, ptrs)
    next_dir = dirs[i % len(dirs)]
    ptrs = [left if next_dir == 'L' else right for (left, right) in [graph[p] for p in ptrs]]
    i += 1

print('Part 2:', i)