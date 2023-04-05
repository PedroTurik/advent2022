with open('input1.txt') as f:
    games = []
    for row in f.readlines():
        games.append(row.strip().split())



points = 0

for o, m in games:
    if o == 'A':
        if m == 'X':
            points += 3
        elif m == 'Y':
            points += 4
        else:
            points += 8
    if o == 'B':
        if m == 'X':
            points += 1
        elif m == 'Y':
            points += 5
        else:
            points += 9
    if o == 'C':
        if m == 'X':
            points += 2
        elif m == 'Y':
            points += 6
        else:
            points += 7
print(points)

