from functools import reduce
with open('input1.txt') as f:
    matrix = [[int(x) for x in row.strip()] for row in f.readlines()]

Y = len(matrix)
X = len(matrix[0])

scenic_values = {}

def scenic(y, x):
    if (y, x) in scenic_values:
        return scenic_values[(y, x)]

    val = matrix[y][x]
    scenic_values[(y, x)] = 1
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    for dy, dx in directions:
        cur = 0
        while True:
            y_new = y + dy * (cur + 1)
            x_new = x + dx * (cur + 1)
            if not (0 <= y_new < Y and 0 <= x_new < X):
                scenic_values[(y, x)] = reduce(lambda x, y: x * y, [scenic_values[(y, x)]], cur)
                break
            elif matrix[y_new][x_new] >= val:
                scenic_values[(y, x)] = reduce(lambda x, y: x * y, [scenic_values[(y, x)]], cur + 1)
                break
            else:
                cur += 1

    return scenic_values[(y, x)]

max_scenic_value = 0

for y in range(Y):
    for x in range(X):
        max_scenic_value = max(max_scenic_value, scenic(y, x))

print(max_scenic_value)
