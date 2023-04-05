from tqdm import tqdm
from helper import can_all, can_east, can_south, can_north, can_west, count_open_in_square

with open('input.txt') as f:
    coords = [(y, x) for y, row in enumerate(f.readlines()) for x, cell in enumerate(row) if cell == '#']


order = [can_north, can_south, can_west, can_east]

def find_destination(pos):
    if can_all(pos, coords): return pos

    for can_direction in order:
        tmp = can_direction(pos, coords)
        if tmp:
            i,j = tmp
            return (pos[0]+i, pos[1]+j)
    return pos


def round():
    destinations = []
    impossible = set()
    for y, x in coords:
        aux = find_destination((y, x))
        if aux in destinations: impossible.add(aux)
        destinations.append(aux)
    for i, pos in enumerate(coords):
        if destinations[i] not in impossible:
            coords[i] = destinations[i]

for i in tqdm(range(10)):
    round()
    order.append(order.pop(0))


print(count_open_in_square(coords))