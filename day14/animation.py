from time import sleep
import os

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
mi, ma = min([x[0] for line in lines for x in line]), max([x[0] for line in lines for x in line])

def print_matrix():
    os.system('clear')
    for row in matrix[:30]:
        x = [(" " if k == '.' else k) for k in row[mi-1:ma+2]]
        x = [("O" if k == '+' else k) for k in x]
        x = [('\u001b[1m\u001b[101;1m\033[1m\033[96m#\x1b[1;0m' if k == '#' else k) for k in x]
        x = ''.join(x) + '\n'
        print(x)

def place_sand():
    matrix[0][500] = '+'
    curY, curX = 0, 500
    while True:
        try:
            print_matrix()
            sleep(0.02)
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

while place_sand():
    pass







