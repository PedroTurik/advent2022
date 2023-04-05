from itertools import zip_longest
from functools import cmp_to_key

with open('input.txt') as f:
    packets = [eval(x.strip()) for x in f.readlines() if x != '\n']


def compare(left, right):
    if not left and right: return True
    if not right and left: return False
    for i, (ln, rn) in enumerate(zip_longest(left,right, fillvalue=None)):
        if   i >= len(left):  return True
        elif i >= len(right): return False
        
        if type(ln) == type(rn) == int:
            if   ln > rn: return False
            elif ln < rn: return True
        
        else:
            if   type(ln) == int: ln = [ln]
            elif type(rn) == int: rn = [rn]
            checker = compare(ln, rn)
            if checker != "keep":
                if checker: return True
                else: return False
    return "keep"

packets.append([[2]])
packets.append([[6]])


ordered_packets = []
for pack in packets:
    for i, cur in enumerate(ordered_packets):
        if compare(pack, cur):
            ordered_packets.insert(i, pack)
            break
    else:
        ordered_packets.append(pack)

a = ordered_packets.index([[6]])+1
b = ordered_packets.index([[2]])+1

for i in range(1, len(ordered_packets)):
    if not compare(ordered_packets[i-1], ordered_packets[i]):
        raise ValueError

print(a*b, a, b)