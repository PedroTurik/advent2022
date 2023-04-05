with open('input.txt') as f:
    monkeys = {k: v.split() for row in f.readlines() for k, v in [row.split(': ')]}
    monkeys['root'][1] = '=='

def get_scream(monkey):
    aux = monkeys[monkey]
    if len(aux)==1: return int(aux[0])
    else:
        if aux[1] == '+': return get_scream(aux[0]) + get_scream(aux[2])
        elif aux[1] == '-': return get_scream(aux[0]) - get_scream(aux[2])
        elif aux[1] == '*': return get_scream(aux[0]) * get_scream(aux[2])
        elif aux[1] == '/': return get_scream(aux[0]) / get_scream(aux[2])
        else: return get_scream(aux[0]) > get_scream(aux[2])

i   = 1000000000000
cur = 1000000000000
monkeys['humn'] = [str(cur)]
while i > 0:
    while get_scream('root'):
        cur += i
        monkeys['humn'] = [str(cur)]
    cur -= i
    i //= 10
    monkeys['humn'] = [str(cur)]

print(cur+1)