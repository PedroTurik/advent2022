from tqdm import tqdm


with open('input.txt') as f:
    sequence = [int(x)*811589153 for x in f.readlines()]

original_order = [x for x in sequence]

for _ in tqdm(range(10)):
    order = [x for x in original_order]
    i = 0
    while order:
        if sequence[i] == order[0]:
            tmp = sequence.pop(i)
            sequence.insert((i+tmp)%len(sequence), tmp)
            order.pop(0)
        else:
            i += 1

ans = []
begin = sequence.index(0)
i = 0
while i <= begin+3000:
    i += 1
    if i%1000 == 0:
        ans.append(sequence[(begin+i)%len(sequence)])
    if len(ans) == 3: break
    


print(sum(ans))
