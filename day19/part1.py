from copy import deepcopy
from math import ceil
from tqdm import tqdm

p_input = open("input.txt", "r")
data = [row.strip() for row in p_input]
p_input.close()

blueprints = []

for d in data:
    tmp = d.split(": ")[1]
    tmp = tmp.split(" ")
    final = ((int(tmp[4]),0,0),(int(tmp[10]), 0, 0),(int(tmp[16]), int(tmp[19]), 0), (int(tmp[25]),0 , int(tmp[28])))
    true_final = (final, (max(final[0][0], final[1][0], final[2][0], final[3][0]), max(final[0][1], final[1][1], final[2][1], final[0][1],final[3][1]), max(final[0][2], final[1][2], final[2][2], final[3][2])))
    blueprints.append(true_final)

#bp format:
# ((ore needed, clay needed, obisidian needed) for every robot, (most ore, most clay, most obisidian))

def waitMinute(minutes, materials, robots, bp, robot):
    for r in range(len(robots)):
        materials[r] += robots[r] * minutes
        materials[r] -= bp[0][robot][r] if r != 3 else 0
    return materials

#all actions are ALWAYS make a robot or wait x minutes to make a robot
#actions return format -> set of (minutes_taken, robot made (index))
def actions(min_left, robots, materials, bp):
    moves = set()
    enough = isEnough(robots,bp)
    for e in range(len(enough)):
        if enough[e]:
            continue
        tmp_min = minutesNeeded(e, robots, materials, bp)
        if tmp_min < min_left:
            moves.add((tmp_min, e))
    if len(moves) == 0:
        return {(min_left, 0)}
    return moves
    
def isEnough(robots,bp):
    ans = list()
    for r in range(len(robots)-1):
        if robots[r] == bp[1][r]:
            ans.append(True)
        else:
            ans.append(False)
    ans.append(False)
    return ans

def minutesNeeded(robot ,robots, material, bp):
    required = [bp[0][robot][x] - material[x] for x in range(3)]
    for r in required:
        if r > 0:
            break
    else:
        return 1
    max_val = 0
    for r in range(len(required)):
        if required[r] > 0:
            if robots[r] > 0:
                max_val = max(max_val,required[r]/robots[r])
            else:
                return 1000000000
    if max_val == 0:
        return 10000000
    return ceil(max_val+1)

def checkBestOutcome(min_left, robots, materials, bp):
    if min_left == 0:
        return materials[3]
    max_val = 0 
    for a in actions(min_left, robots, materials, bp):
        ml, rt = a
        tmp_robots = deepcopy(robots)
        tmp_robots[rt] += 1
        tmp_material = deepcopy(materials)
        tmp = checkBestOutcome(min_left - ml, tmp_robots, waitMinute(ml, tmp_material, robots, bp, rt), bp)
        max_val = max(tmp, max_val)
    return max_val

counter = 0
for bp in tqdm(range(0,len(blueprints))):
    counter += checkBestOutcome(24, [1,0,0,0], [0,0,0,0], blueprints[bp])*(bp+1)

print(counter)