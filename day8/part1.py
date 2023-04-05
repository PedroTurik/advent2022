with open('input1.txt') as f:
    matrix = [[int(x) for x in row.strip()] for row in f.readlines()]

Y = len(matrix)
X = len(matrix[0])

def is_visible(y, x):
    val = matrix[y][x]

    for i in range(x-1, -1, -1):
        if matrix[y][i] >= val:
            break
    else:
        return True

    for i in range(y-1, -1, -1):
        if matrix[i][x] >= val:
            break
    else:
        return True

    for i in range(x+1, X):
        if matrix[y][i] >= val:
            break
    else:
        return True

    for i in range(y+1, Y):
        if matrix[i][x] >= val:
            break
    else:
        return True

    return False

counter = 0
for y in range(Y):
    for x in range(X):
        if 0 in (y,x) or x == X-1 or y == Y-1:
            counter += 1
            continue
        if is_visible(y, x):
            counter += 1

print(counter)