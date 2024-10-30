# https://www.acmicpc.net/problem/15686

import sys

answer = sys.maxsize

def dfs(i, cnt):
    global M, C, H, answer
    visited[i] = 1

    if cnt == M:
        l = [sys.maxsize for _ in range(H)]
        for i in range(H):
            for j in range(C):
                if visited[j] == 1 and l[i] > infos[i][j]:
                    l[i] = infos[i][j]
        
        if answer > sum(l):
            answer = sum(l)
            return

    
    else:
        for j in range(i + 1, C): # 셰프의 킥 ~ 뒤로 돌아가서 볼 필요는 업쥬
            if visited[j] == 0:
                dfs(j, cnt + 1)
                visited[j] = 0

N, M = map(int, sys.stdin.readline().split())
arr = [] # 도시 정보

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

chicks = []
homes = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            homes.append([i, j])
        elif arr[i][j] == 2:
            chicks.append([i, j])

infos = []

for home in homes:
    info = []
    for chick in chicks:
        info.append(abs(home[0] - chick[0]) + abs(home[1] - chick[1]))
    
    infos.append(info)

C = len(chicks)
H = len(homes)

for i in range(C):
    visited = [0 for _ in range(C)]
    dfs(i, 1)

print(answer)