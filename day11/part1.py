from day11.Monkey import Monkey

monkeys = [
    Monkey([83, 97, 95, 67],                 lambda x: x*19, lambda x: (True if x%17==0 else False), 2, 7),
    Monkey([71, 70, 79, 88, 56, 70],         lambda x: x+2,  lambda x: (True if x%19==0 else False), 7, 0),
    Monkey([98, 51, 51, 63, 80, 85, 84, 95], lambda x: x+7,  lambda x: (True if x%7 ==0 else False), 4, 3),
    Monkey([77, 90, 82, 80, 79],             lambda x: x+1,  lambda x: (True if x%11==0 else False), 6, 4),
    Monkey([68],                             lambda x: x*5,  lambda x: (True if x%13==0 else False), 6, 5),
    Monkey([60, 94],                         lambda x: x+5,  lambda x: (True if x%3 ==0 else False), 1, 0),
    Monkey([81, 51, 85],                     lambda x: x*x,  lambda x: (True if x%5 ==0 else False), 5, 1),
    Monkey([98, 81, 63, 65, 84, 71, 84],     lambda x: x+3,  lambda x: (True if x%2 ==0 else False), 2, 3)
]

inspections= [0 for _ in range(8)]

for _ in range(20):
    for i, monkey in enumerate(monkeys):
        while monkey.items:
            item, where = monkey.inspect()
            inspections[i] += 1
            monkeys[where].add(item)


inspections.sort()
print(inspections[-1]*inspections[-2])