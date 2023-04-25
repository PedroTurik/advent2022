def parser(file):
    with open(file) as f:
        input = f.read().split("\n\n")

    top_side = input[0].split('\n')
    bottom_side = [row.split() for row in input[1].split('\n')]
    
    number_of_stacks = int(top_side[-1].split()[-1])
    horizontal_stacks = top_side[:-1]

    stacks = [[] for _ in range(number_of_stacks)]
    for row in horizontal_stacks:
        for i in range(1, len(row), 4):
            if row[i] != ' ':
                stacks[i//4].append(row[i])


    commands = [(int(row[1]), int(row[3]), int(row[5])) for row in bottom_side]

    return [list(reversed(a)) for a in stacks], commands

