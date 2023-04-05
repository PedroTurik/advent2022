with open('input.txt') as f:
    commands = [x.split() for x in f.readlines()]

interestin_cycles = {x for x in range(20, 221, 40)}
cycle = 0
registerX = 1
ans = 0
for command in commands:
    if command[0] == 'noop':
        cycle += 1
        if cycle in interestin_cycles: 
            ans += (registerX*cycle)
        continue
    else:
        for i in range(2):
            cycle += 1
            if cycle in interestin_cycles:
                ans += (registerX*cycle)
        registerX += int(command[1])
            



print(ans)