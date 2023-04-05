with open('input1.txt') as f:
    elves = f.readlines()

hi_elf = []
cur_elf = []

for row in elves:
    if row.strip() == '':
        hi_elf.append(sum(cur_elf))
        cur_elf = []
    else:
        cur_elf.append(int(row.strip()))

hi_elf.sort()
print(sum(hi_elf[-3:]))