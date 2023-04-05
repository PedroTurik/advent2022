from time import time


with open('input.txt') as f:
    sensors = {(int(y1[2:-1]), int(x1[2:-1])): (int(y2[2:]), int(x2[2:-1])) for row in f.readlines() for _,_,x1,y1,_,_,_,_,x2,y2 in [row.split()]}

def manhattan(sy,sx,by,bx):
    return abs(sy-by) + abs(sx - bx)

def is_impossible(y, x):
    for (sy,sx), dist in maxDistances.items():
        if dist >= (abs(sy-y) + abs(sx-x)):
            return (sy,sx)
    return False

 
maxDistances = {(sy, sx): manhattan(sy,sx,by,bx) for (sy,sx), (by,bx) in sensors.items()}

st = time()
y,x = 0, 0
while y < 4000001:
    if x > 4000000:
        x, y = 0, y+1
    cord = is_impossible(y, x)
    if cord:
        if x < cord[1]: x = cord[1]
        x += maxDistances[cord] - manhattan(cord[0], cord[1], y, x)
    else:
        print(x*4000000 + y)
        break
    x += 1

print(st - time())