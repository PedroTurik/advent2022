with open('input.txt') as f:
    commands = [x.split() for x in f.readlines()]


screen = ['.' for _ in range(240)]


cur_draw = 0
registerX = 1
i = 1
for command in commands:
    if cur_draw >= 240: break
    if cur_draw >= 40*i:
        i += 1
        registerX += 40
    if command[0] == 'addx':
        if registerX-1 <= cur_draw <= registerX+1:
            screen[cur_draw] = '#'
        cur_draw += 1
        if registerX-1 <= cur_draw <= registerX+1:
            screen[cur_draw] = '#'
        registerX += int(command[1])
        cur_draw += 1
    else:
        if registerX-1 <= cur_draw <= registerX+1:
            screen[cur_draw] = '#'
        cur_draw += 1

print(screen)

matrix = []
aux = []
for c in screen:
    aux.append(c)
    if len(aux) == 40:
        matrix.append(aux)
        aux = []

for row in matrix:
    print(row)
