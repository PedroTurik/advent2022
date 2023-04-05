from collections import defaultdict

def calculate_sum(key, dir):
    if type(key) == int: return key
    return sum([calculate_sum(x, dir) for x in dir[key]])

def distinct_parser(file):
    knownDIR = defaultdict(int)
    with open(file) as f:
        lines = [a.strip().split() for a in f.readlines()]
    for line in lines:
        idx = len(line) - 1
        for flag in ['cd', 'dir']:
            if line[idx-1] == flag:
                aux = knownDIR[line[idx]]
                if flag == 'cd': knownDIR[line[idx]] += 1
                if aux:
                    line[idx] += str(aux)
    return lines
        