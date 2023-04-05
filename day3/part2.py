with open('input1.txt') as f:
    lines = [{c for c in row.strip()} for row in f.readlines()]

print(sum([ord([a for a in lines[i].intersection(lines[i-1], lines[i-2])][0]) - (96 if [a for a in lines[i].intersection(lines[i-1], lines[i-2])][0].islower() else 38) for i in range(2, len(lines), 3)]))