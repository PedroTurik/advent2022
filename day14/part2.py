with open('input.txt') as f:
    lines = [[list(map(int, x.split(','))) for x in row.strip().split(' -> ')] for row in f.readlines()]


matrix = [['.' for _ in range(1000)] for b in range(1000)]
floor = max([x[1] for line in lines for x in line]) + 2

for i in range(len(matrix[0])):
    matrix[floor][i] = '#'


for line in lines:
    for i, (x, y) in enumerate(line[1:]):
        sx, sy = line[i]
        if x == sx:
            if sy > y: sy, y = y, sy
            for i in range(sy, y+1):
                matrix[i][x] = '#'
        if y == sy:
            if sx > x: sx, x = x, sx
            for i in range(sx, x+1):
                matrix[y][i] = '#'


def place_sand():
    matrix[0][500] = '+'
    curY, curX = 0, 500
    while True:
        if matrix[curY+1][curX] == '.':
            matrix[curY+1][curX] = '+'
            matrix[curY][curX] = '.'
            curY += 1
        elif matrix[curY+1][curX-1] == '.':
            matrix[curY+1][curX-1] = '+'
            matrix[curY][curX] = '.'
            curY += 1
            curX -= 1
        elif matrix[curY+1][curX+1] == '.':
            matrix[curY+1][curX+1] = '+'
            matrix[curY][curX] = '.'
            curY += 1
            curX += 1
        else:
            return True


counter = 0
while matrix[0][500] != '+':
    place_sand()
    counter += 1

print(counter)