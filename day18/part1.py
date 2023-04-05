with open('input.txt') as f:
    cubes = [(int(x), int(y), int(z)) for row in f.readlines() for x,y,z in [row.strip().split(',')]]

surface_area = 0
for x,y,z in cubes:
    cur_surf = 6
    for x2,y2,z2 in cubes:
        soma = abs(x-x2) + abs(y-y2) + abs(z-z2)
        if soma == 0: continue

        if soma == 1:
            cur_surf -= 1
    surface_area += cur_surf

print(surface_area)