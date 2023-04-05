from adv_parser import get_data

board, commands = get_data('input.txt')

orientations = [(1, 1), (0, 1), (1,-1), (0, -1)]
cur_orientation = 0

pos = [0, 50]

a1 = {(k+150, -1, 2): (0, k+50, 1) for k in range(50)}
a2 = {(-1, k+50, 3): (k+150, 0, 0) for k in range(50)}
b1 = {(200, k, 1): (0, k+100, 1) for k in range(50)}
b2 = {(-1, k+100, 3): (199, k, 3) for k in range(50)}
c1 = {(k+100, 100, 0): (49-k, 149, 2) for k in range(50)}
c2 = {(49-k, 150, 0): (k+100, 99, 2) for k in range(50)}
d1 = {(k+50, 100, 0): (49, k+100, 3) for k in range(50)}
d2 = {(50, k+100, 1): (k+50, 99, 2) for k in range(50)}
e1 = {(k+150, 50, 0): (149, k+50, 3) for k in range(50)}
e2 = {(150, k+50, 1): (k+150, 49, 2) for k in range(50)}
f1 = {(k+100, -1, 2): (49-k, 50, 0) for k in range(50)}
f2 = {(49-k, 49, 2): (k+100, 0, 0) for k in range(50)}
g1 = {(99, k, 3): (k+50, 50, 0) for k in range(50)}
g2 = {(k+50, 49, 2): (100, k, 1) for k in range(50)}

dict_list = [a1,a2,b1,b2,c1,c2,d1,d2,e1,e2,f1,f2,g1,g2]

edges = {}
for dic in dict_list:
    for k, v in dic.items():
        edges[k] = v

def check_wrap():
    global pos
    global cur_orientation
    wrap_info = edges.get((pos[0], pos[1], cur_orientation), False)
    if wrap_info:
        if board[wrap_info[0]][wrap_info[1]] == '.':
            pos = [wrap_info[0], wrap_info[1]]
            cur_orientation = wrap_info[2]
        else:
            return False
    return True
            
def is_wall():
    return board[pos[0]][pos[1]] == '#'



def move(steps):
    for _ in range(steps):
        i, d = orientations[cur_orientation]
        pos[i] += d
        if not check_wrap() or is_wall():
            pos[i] -= d
            break

for i, command in enumerate(commands):
    if i%2==0:
        move(command)
    else:
        cur_orientation = (cur_orientation+command)%4

print(1000*(pos[0]+1) + 4*(pos[1]+1) + cur_orientation)

for i, c in enumerate(board[0]):
    if c == '.':
        print(i)
        break
