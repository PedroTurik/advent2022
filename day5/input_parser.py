import re

def parser(file):
    with open(file) as f:
        input = f.read().split("\n\n")
        inp_stacks = input[0].split('\n')[:-1]


    n_of_stacks = int(re.split("\s+" ,input[0])[-2])
    inp_stacks = input[0].split('\n')[:-1]
    commands = [[int(x.split()[i]) for i in range(1,6,2)] for x in input[1].split('\n')]
    stacks = [[] for _ in range(n_of_stacks)]

    for line in inp_stacks:
        index = 1
        stack = 0
        l = len(line)
        while index < l:
            letter = line[index]
            if letter.isalpha():
                stacks[stack].append(letter)
            index += 4
            stack += 1

    return [list(reversed(a)) for a in stacks], commands







