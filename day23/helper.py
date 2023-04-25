def count_open_in_square(coords):
    maxY = maxX = 0
    minY = minX = 10000000
    for y, x in coords:
        if y > maxY: maxY = y
        if y < minY: minY = y
        if x > maxX: maxX = x
        if x < minX: minX = x
    return (maxY-minY+1)*(maxX-minX+1) - len(coords)

