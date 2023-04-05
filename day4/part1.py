with open('input1.txt') as f:
    lines = [a.strip() for a in f.readlines()]
    lines = [b.split(',') for b in lines]
    for i, (f, s) in enumerate(lines):
        lines[i][0], lines[i][1] = list(map(int, f.split('-'))), list(map(int, s.split('-') ))
    
counter = 0
for f, s in lines:
    if (f[0] <= s[0] and f[1] >= s[1]) and (f[0] >= s[0] and f[1] <= s[1]):
        counter += 1  
print(counter)