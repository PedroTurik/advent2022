with open('input.txt') as f:
    commands = [row.split() for row in f.readlines()]

def is_touching(head, tail):
    hy, hx = head
    ty, tx = tail
    xmod = abs(hx - tx)
    ymod = abs(hy - ty)
    return xmod <= 1 and ymod <= 1

matrix = [[0 for _ in range(1000)] for x in range(1000)]
rope = [[500, 500] for _ in range(10)]
matrix[500][500] = 1

def move_rope():
    for i in range(1,10):
        ay, ax = rope[i-1]
        by, bx = rope[i]
        if is_touching(rope[i-1], rope[i]):
            break
        elif ay == by:
            rope[i][1] += (1 if ax > bx else -1)
        elif ax == bx:
            rope[i][0] += (1 if ay > by else -1)
        else:
            rope[i][0] += (1 if ay > by else -1)
            rope[i][1] += (1 if ax > bx else -1)


def move(d, s, n):
    for _ in range(n):
        rope[0][d] += s
        move_rope()
        matrix[rope[-1][0]][rope[-1][1]] += 1



for direction, n in commands:
    if   direction == 'R': move(1, 1, int(n)) 
    elif direction == 'L': move(1, -1, int(n)) 
    elif direction == 'U': move(0, 1, int(n))
    elif direction == 'D': move(0, -1, int(n))


print(sum(1 for y in matrix for x in y if x > 0))