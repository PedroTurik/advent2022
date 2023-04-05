import sys

sys.setrecursionlimit(5000)

with open('input.txt') as f:
    cubes = [(int(x), int(y), int(z)) for row in f.readlines() for x,y,z in [row.strip().split(',')]]

big_cube = [[[0 for _ in range(22)] for _ in range(22)] for _ in range(22)]

for x,y,z in cubes:
    big_cube[y][x][z] = 1

def dive(y, x, z):
    if big_cube[y][x][z] == 0:
        big_cube[y][x][z] = 2

        if y > 0:  dive(y - 1, x, z)
        if y < 21: dive(y + 1, x, z)
        if x > 0:  dive(y, x - 1, z)
        if x < 21: dive(y, x + 1, z)
        if z > 0:  dive(y, x, z - 1)
        if z < 21: dive(y, x, z + 1)



for y in range(22):
    for x in range(22):
        for z in range(22):
            if (y != 0 and y != 21) and (x != 0 and x != 21) and (z != 0 and z != 21):
                continue

            if big_cube[y][x][z] == 0: dive(y, x, z)

locked = set()     
for y in range(22):
    for x in range(22):
        for z in range(22):
            if big_cube[y][x][z] == 0:
                locked.add((y,x,z))


surface_area = 0
for x,y,z in locked:
    cur_surf = 6
    for x2,y2,z2 in locked:
        soma = abs(x-x2) + abs(y-y2) + abs(z-z2)
        if soma == 0: continue

        if soma == 1:
            cur_surf -= 1
    surface_area += cur_surf

print(4244- surface_area)