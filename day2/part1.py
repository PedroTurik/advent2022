with open('input1.txt') as f:
    games = []
    for row in f.readlines():
        games.append(row.strip().split())



points = 0

for o, m in games:
    if m == 'X':
        points += 1
        if o == 'A':
            points += 3
        elif o == 'C':
            points += 6
    if m == 'Y':
        points += 2
        if o == 'A':
            points += 6
        elif o == 'B':
            points += 3

    if m == 'Z':
        points += 3
        if o == 'B':
            points += 6
        elif o == 'C':
            points += 3

print(points)



