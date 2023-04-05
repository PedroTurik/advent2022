with open('input.txt') as f:
    data = [x.replace(':',"=") for x in f.readlines()]

while True:
    explored = set()
    while "root" not in explored:
        for d in data:
            try:
                exec(d)
                explored.add(d.split("=")[0])
            except NameError:
                pass
    if root:
        break
    if tcmj > qggp:
        i = int(str(i)[:idx_at_moment] + str(int(str(i)[idx_at_moment])+1) + str(i)[idx_at_moment+1:])
        if str(i)[idx_at_moment] == "9":
            idx_at_moment += 1
    elif tcmj < qggp:
        i = int(str(i)[:idx_at_moment] + str(int(str(i)[idx_at_moment])-1) + str(i)[idx_at_moment+1:])
        idx_at_moment += 1
    for e in explored:
        exec(f"del {e}")