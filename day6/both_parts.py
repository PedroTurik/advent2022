with open('input1.txt') as f:
    device = f.readline().strip()

def solve(device, n):
    ans = 0
    last_four = []
    for c in device:
        ans += 1
        while c in last_four:
            last_four.pop(0)
        last_four.append(c)
        if len(last_four) == n:
            break
    print(ans)

solve(device, 4)
solve(device, 14)