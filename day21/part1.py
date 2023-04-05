from tqdm import tqdm


with open('input.txt') as f:
    monkeys = [x.replace(':',"=") for x in f.readlines()]
i = 0
executed = set()
while True:
    if len(executed) == len(monkeys): break
    try:
        if monkeys[i%len(monkeys)] not in executed:
            exec(monkeys[i%len(monkeys)])
            executed.add(monkeys[i%len(monkeys)])
    except NameError:
        pass
    i += 1

print(root)