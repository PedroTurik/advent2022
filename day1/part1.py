with open('input1.txt') as f:
    elves = f.readlines()

hi_elf = 0
cur_elf = 0

for row in elves:
    if row.strip() == '':
        if cur_elf > hi_elf:
            hi_elf = cur_elf
        cur_elf = 0
    else:
        cur_elf += int(row.strip())

print(hi_elf)