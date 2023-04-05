from itertools import zip_longest

with open('input.txt') as f:
    pairs = [line.split('\n') for line in f.read().split('\n\n')]

for i, pair in enumerate(pairs):
    pairs[i] = list(map(eval, pair))

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
        

ans = []

for i, (left, right) in enumerate(pairs, start=1):
    if compare(left, right):
        ans.append(i)

print(ans, sum(ans))