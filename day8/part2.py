with open('input1.txt') as f:
    matrix = [[int(x) for x in row.strip()] for row in f.readlines()]

Y = len(matrix)
X = len(matrix[0])

def scenic(y, x):
    val = matrix[y][x]
    scenic_values = []
    cur = 0
    for i in range(x-1, -1, -1):
        if matrix[y][i] >= val:
            scenic_values.append(cur+1)
            break
        else:
            cur += 1
    else:
        scenic_values.append(cur)

    cur = 0
    for i in range(y-1, -1, -1):
        if matrix[i][x] >= val:
            scenic_values.append(cur+1)
            break
        else:
            cur += 1
    else:
        scenic_values.append(cur)

    cur = 0
    for i in range(x+1, X):
        if matrix[y][i] >= val:
            scenic_values.append(cur+1)
            break
        else:
            cur += 1
    else:
        scenic_values.append(cur)

    cur = 0
    for i in range(y+1, Y):
        if matrix[i][x] >= val:
            scenic_values.append(cur+1)
            break
        else:
            cur += 1
    else:
        scenic_values.append(cur)
    
    ans = 1
    for k in scenic_values:
        ans *= k
    return ans


print(max([scenic(y, x) for y in range(Y) for x in range(X)]))