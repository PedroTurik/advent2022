with open('input.txt') as f:
    lines = [[list(map(int, x.split(','))) for x in row.strip().split(' -> ')] for row in f.readlines()]


matrix = [['.' for _ in range(1000)] for b in range(1000)]

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
        try:
            next_places = [(curY+1, curX), (curY+1, curX-1), (curY+1, curX+1)]
            for y, x in next_places:
                if matrix[y][x] == '.':
                    matrix[y][x] = '+'
                    matrix[curY][curX] = '.'
                    curY, curX = y, x
                    break
            else:
                return True
        except IndexError:
            return False

counter = 0
while place_sand():
    counter += 1

print(counter)


