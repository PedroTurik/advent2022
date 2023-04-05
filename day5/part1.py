from input_parser import parser

lines, commands = parser('full-input.txt')


for qtd, f, t in commands:
    for _ in range(qtd):
        aux = lines[f-1].pop()
        lines[t-1].append(aux)

for line in lines:
    print(line[-1], end='')