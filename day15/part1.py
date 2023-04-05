with open('input.txt') as f:
    sensors = {(int(y1[2:-1]), int(x1[2:-1])): (int(y2[2:]), int(x2[2:-1])) for row in f.readlines() for _,_,x1,y1,_,_,_,_,x2,y2 in [row.split()]}

impossiblePoints = set()
beaconsAtRow = set()

def rowReach(sy, sx, by, bx, row):
    return (abs(sy-by) + abs(sx-bx)) - abs(sy - row)


def addPoints(sx, reach):
    for i in range(sx-reach, sx+reach+1):
        impossiblePoints.add(i)


for (sy, sx), (by, bx) in sensors.items():
    if by == 2000000: beaconsAtRow.add(bx)
    reach = rowReach(sy, sx, by, bx, 2000000)
    if reach >= 0:
        addPoints(sx, reach)

print(len(impossiblePoints) - len(beaconsAtRow))