from helper import block, reverse_l, four_line, plus_sign, vertical_line

with open('teste.txt') as f:
    jets = ''.join(f.readlines())

matrix = [[0 for _ in range(7)] for _ in range(5400)]
cur_jet = 0
modjets = len(jets)
cycle = [four_line, plus_sign, reverse_l, vertical_line, block]
cur_shape = 0
cur_height = -4

for _ in range(2022):
    cur = cycle[cur_shape % 5](matrix, cur_height)
    while True:
        cur.moveLeft() if jets[cur_jet % modjets] == '<' else cur.moveRight()
        cur_jet += 1
        if not cur.moveDown():
            break

    newHeight = cur.getNewHeight()
    if newHeight < cur_height: cur_height = newHeight
    cur.markMatrix()
    cur_shape += 1        

print(cur_height + 4)

for row in matrix:
    if sum(row) == 7:
        print(row)