from collections import defaultdict
from typing import List

from helper import distinct_parser, calculate_sum

dir = defaultdict(list)

lines = distinct_parser('input1.txt')
occupied = sum([int(x) for row in lines for x in row if x.isnumeric()])

for idx, line in enumerate(lines):
    if line[1] == 'ls':
        l: list[str]
        for l in lines[idx + 1:]:
            if l[0] == '$':
                break
            elif l[0].isnumeric():
                dir[lines[idx - 1][2]].append(int(l[0]))
            elif l[0] == 'dir':
                dir[lines[idx - 1][2]].append(l[1])

print(sum(x for p in dir for x in [calculate_sum(p, dir)] if x <= 100000))

print(min([n for n in sorted([calculate_sum(x, dir) for x in dir]) if occupied - n <= 40000000]))
