def is_neighbor(pos, y, x):
    if (y == pos[0]-1 and pos[1]-1 <= x <= pos[1]+1) or \
        (y == pos[0]+1 and pos[1]-1 <= x <= pos[1]+1) or \
        (y == pos[0] and (x == pos[1]-1 or x == pos[1]+1)):
        return True
    return False

def can_north(pos, y, x):
    if y == pos[0]-1 and pos[1]-1 <= x <= pos[1]+1:
        return False
    return (-1, 0)
def can_south(pos, y, x):
    if y == pos[0]+1 and pos[1]-1 <= x <= pos[1]+1:
        return False
    return (+1, 0)
def can_west(pos, y, x):
    if x == pos[1]-1 and pos[0]-1 <= y <= pos[0]+1:
        return False
    return (0, -1)
def can_east(pos, y, x):
    if x == pos[1]+1 and pos[0]-1 <= y <= pos[0]+1:
        return False
    return (0, +1)

def count_open_in_square(coords):
    maxY = maxX = 0
    minY = minX = 10000000
    for y, x in coords:
        if y > maxY: maxY = y
        if y < minY: minY = y
        if x > maxX: maxX = x
        if x < minX: minX = x
    return (maxY-minY+1)*(maxX-minX+1) - len(coords)

