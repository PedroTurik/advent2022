from tqdm import tqdm
from helper import block, reverse_l, four_line, plus_sign, vertical_line

with open('input.txt') as f:
    jets = ''.join(f.readlines())

matrix = [[0 for _ in range(7)] for _ in range(54000)]
cur_jet = 0
modjets = len(jets)
cycle = [four_line, plus_sign, reverse_l, vertical_line, block]
cur_shape = 0
cur_height = -4

for _ in tqdm(range(20220)):
    if cur_shape == 5: cur_shape = 0
    cur = cycle[cur_shape](matrix, cur_height)
    while True:
        if jets[cur_jet] == '<':
            cur.moveLeft()
        else:
            cur.moveRight()
        cur_jet += 1
        if cur_jet == modjets: cur_jet = 0
        if not cur.moveDown():
            break
    if cur_jet == 0:
        print(matrix[cur_height:])
        break


    newHeight = cur.getNewHeight()
    if newHeight < cur_height: cur_height = newHeight
    cur.markMatrix()
    cur_shape += 1        



binary_rows = []

for row in tqdm(reversed(matrix)):
    if sum(row) == 0:
        break
    binary_rows.append(int(''.join(list(map(str, row))), 2))

with open('buffer.txt', 'w') as f:
    f.write(str(binary_rows))

