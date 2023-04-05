with open('input.txt') as f:
    grid = [[letter for letter in row.strip()] for row in f.readlines()]

Y = len(grid)
X = len(grid[0])

starts = []
for y, row in enumerate(grid):
    for x, n in enumerate(row):
        if n == 'S' or n == 'a':
            starts.append((y,x))
        elif n == 'E':
            end = (y, x)
closestPath = 10000000
while starts:
    start = starts.pop()
    queue = [start, 0]
    visited = set()
    while queue:
        cur = queue.pop(0)
        count = queue.pop(0)
        if cur == end: break
        y, x = cur
        cur_height = grid[y][x]
        cur_val = 100 if cur_height == 'S' else ord(cur_height)

        for i, j in [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]:
            if 0 <= i < Y and 0 <= j < X:
                if ord(grid[i][j]) <= cur_val+1 and (i,j) not in visited:
                    queue.append((i,j))
                    visited.add((i,j))
                    queue.append(count+1)
    if count < closestPath and cur == end:
        closestPath = count

print(closestPath)