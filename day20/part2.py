with open('input.txt') as f:
    sequence = [(int(x)*811589153, i) for i, x in enumerate(f.readlines())]

original_order = [x for x in sequence]
zero = [x for x in sequence if x[0] == 0][0]

for _ in range(10):
    order = [x for x in original_order]
    while order:
        cur = order.pop(0)
        i = sequence.index(cur)
        sequence.pop(i)
        sequence.insert((i+cur[0])%len(sequence), cur)

ans = []
begin = sequence.index(zero)
i = 0
while i <= begin+3000:
    i += 1
    if i%1000 == 0:
        ans.append(sequence[(begin+i)%len(sequence)][0])
    if len(ans) == 3: break
    


print(sum(ans))

