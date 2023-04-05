with open('input.txt') as f:
    commands = [row.split() for row in f.readlines()]

def is_touching(head, tail):
    hy, hx = head
    ty, tx = tail
    xmod = abs(hx - tx)
    ymod = abs(hy - ty)
    return xmod <= 1 and ymod <= 1

matrix = [[0 for _ in range(1000)] for x in range(1000)]

head = [500,500]
tail = [500,500]
matrix[500][500] = 1

def move(d, s, n):
    for _ in range(n):
        oldy, oldx = head
        head[d] += s
        if not is_touching(head, tail):
            tail[0], tail[1] = oldy, oldx
            matrix[oldy][oldx] += 1


for direction, n in commands:
    if   direction == 'R': move(1, 1, int(n)) 
    elif direction == 'L': move(1, -1, int(n)) 
    elif direction == 'U': move(0, 1, int(n))
    elif direction == 'D': move(0, -1, int(n))


print(sum(1 for y in matrix for x in y if x > 0))