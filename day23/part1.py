from tqdm import tqdm
from helper import count_open_in_square

with open('input.txt') as f:
    coords = {(y, x) for y, row in enumerate(f.readlines()) for x, cell in enumerate(row) if cell == '#'}

class Dir():
    North = (-1, 0)
    South = (1, 0)
    West = (0, -1)
    East = (0, +1)


def can_all(pos):
    info = {}

    for i in range(-1, 2):
        if (pos[0] - 1, pos[1] + i) in coords:
            info[Dir.North] = True
            break
    else:
        info[Dir.North] = False
    
    for i in range(-1, 2):
        if (pos[0] + 1, pos[1] + i) in coords:
            info[Dir.South] = True
            break
    else:
        info[Dir.South] = False
    
    for i in range(-1, 2):
        if (pos[0] + i, pos[1] - 1) in coords:
            info[Dir.West] = True
            break
    else:
        info[Dir.West] = False
    
    for i in range(-1, 2):
        if (pos[0] + i, pos[1] + 1) in coords:
            info[Dir.East] = True
            break
    else:
        info[Dir.East] = False

    return info
        


    


order = [Dir.North, Dir.South, Dir.West, Dir.East]

def find_destination(pos):
    info = can_all(pos)
    if not any(info.values()): return pos

    for d in order:
        if not info[d]:
            dy, dx = d
            return (pos[0]+dy, pos[1]+dx)
    
    return pos





def round():
    destinations_set = set()
    destinations = {}
    impossible = set()
    for pos in coords:
        aux = find_destination(pos)
        if aux in impossible:
            destinations_set.add(pos)
            continue

        if aux in destinations_set:
            impossible.add(aux)
            destinations_set.add(destinations[aux])
            destinations_set.discard(aux)

        destinations_set.add(aux)
        destinations[aux] = pos

    coords.clear()
    coords

    


for i in tqdm(range(10)):
    round()
    order.append(order.pop(0))


print(count_open_in_square(coords))