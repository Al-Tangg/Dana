# https://www.acmicpc.net/problem/15686

import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
arr = []

chicks = []
homes = []

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            homes.append([i, j])
        elif arr[i][j] == 2:
            chicks.append([i, j])

distance = [[0 for _ in range(len(chicks))] for _ in range(len(homes))]

for i in range(len(homes)):
    h_x, h_y = homes[i]
    for j in range(len(chicks)):
        c_x, c_y = chicks[j]

        distance[i][j] = abs(h_x - c_x) + abs(h_y - c_y)

result = sys.maxsize


for combi in combinations(range(len(chicks)), M):
    dis = 0

    for h in distance:
        min = sys.maxsize

        for c in combi:
            if h[c] < min:
                min = h[c]

        dis += min

    if result > dis:
        result = dis

print(result)
    
