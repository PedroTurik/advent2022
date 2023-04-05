from functools import cache
from sys import setrecursionlimit
from tqdm import tqdm

setrecursionlimit(100000)
with open('teste.txt') as f:
    bl = [
        {
            'id': int(id[:-1]),
            'oreRobotCost': int(oreCost),
            'clayRobotCost': int(clayCost),
            "obsRobotCost": (int(obsCostOre), int(obsCostClay)),
            "geoRobotCost": (int(geoCostOre), int(geoCostObs))
        }
        for _, id, _, _, _, _, oreCost, _, _, _, _, _, clayCost, _, _, _, _, _, obsCostOre, _, _, obsCostClay, _, _, _, _, _, geoCostOre, _, _, geoCostObs, _ in [l.split() for l in f.readlines()]]

maxOre, maxClay, maxObs = 0, 0, 0

@cache
def dfs(s, oreR, clayR, obsR, ore, clay, obs, i):
    if ore == bl[i]["geoRobotCost"][0] and obs == bl[i]["geoRobotCost"][1]:
        ret = 0
        while s > 0:
            s -= 1
            if ore == bl[i]["geoRobotCost"][0] and obs == bl[i]["geoRobotCost"][1]: ret += (s)
            ore -= bl[i]["geoRobotCost"][0]
            obs -= bl[i]["geoRobotCost"][1]
            ore += oreR
            obs += obsR
        return ret
    if s == 0: return 0
    ans = []
    nore = ore + oreR
    nclay = clay + clayR
    nobs = obs + obsR
    ans.append(dfs(s-1, oreR, clayR, obsR, nore, nclay, nobs, i))
    if bl[i]['obsRobotCost'][0] <= ore and bl[i]['obsRobotCost'][1] <= clay and obsR < maxObs:
        ans.append(dfs(s-1, oreR, clayR, obsR+1, nore-bl[i]['obsRobotCost'][0], nclay-bl[i]['obsRobotCost'][1], nobs, i))
    if bl[i]['clayRobotCost'] <= ore and clayR < maxClay:
        ans.append(dfs(s-1, oreR, clayR+1, obsR, nore, nclay-bl[i]['clayRobotCost'], nobs, i))
    if bl[i]['oreRobotCost'] <= ore and oreR < maxOre:
        ans.append(dfs(s-1, oreR+1, clayR, obsR, nore-bl[i]['oreRobotCost'], nclay, nobs, i))
    return max(ans)

ans = 0
for ind in tqdm(range(len(bl))):
    maxOre = max(bl[ind]["oreRobotCost"], bl[ind]["clayRobotCost"], bl[ind]["obsRobotCost"][0], bl[ind]["geoRobotCost"][0])
    maxClay = bl[ind]["obsRobotCost"][1]
    maxObs = bl[ind]["geoRobotCost"][1]
    ans += dfs(24, 1, 0, 0, 0, 0, 0, ind)*bl[ind]['id']

print(ans)
