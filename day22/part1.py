from adv_parser import get_data

board, commands = get_data('input.txt')

for i, c in enumerate(board[0]):
    if c == '.':
        startX = i
        break

orientations = [(1, 1), (0, 1), (1,-1), (0, -1)]
cur_orientation = 0

pos = [0, startX]


def check_wrap(i, d):
    global pos
    tmp_pos = pos.copy()
    if pos[0] == len(board) or pos[1] == len(board[0]) or -1 in pos or board[pos[0]][pos[1]] == '%':
        while True:
            tmp_pos[i] -= d
            if tmp_pos[0] == len(board) or tmp_pos[1] == len(board[0]) or -1 in tmp_pos or board[tmp_pos[0]][tmp_pos[1]] == '%':
                tmp_pos[i] += d
                if board[tmp_pos[0]][tmp_pos[1]] == '#':
                    return False
                else:
                    pos = tmp_pos
                    return True
    else:
        return True
            
def is_wall():
    return board[pos[0]][pos[1]] == '#'



def move(steps):
    i, d = orientations[cur_orientation]
    for _ in range(steps):
        pos[i] += d
        if not check_wrap(i, d):
            pos[i] -= d
            break
        if is_wall():
            pos[i] -= d
            break


for i, command in enumerate(commands):
    if i%2==0:
        move(command)
    else:
        cur_orientation = (cur_orientation+command)%4


print(1000*(pos[0]+1) + 4*(pos[1]+1) + cur_orientation)
