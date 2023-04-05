from input_parser import parser

lines, commands = parser('full-input.txt')


for qtd, f, t in commands:
    l = len(lines[t-1])
    for _ in range(qtd):
        aux = lines[f-1].pop()
        lines[t-1].insert(l, aux)

for line in lines:
    print(line[-1], end='')