# https://www.acmicpc.net/problem/14502

import sys
from itertools import combinations
from collections import deque

# 0 빈칸, 1 벽, 2 바이러스

N, M = map(int, sys.stdin.readline().split())
arr = []

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

zeros = []

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            zeros.append([i, j])

answer = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for combi in combinations(zeros, 3):
    tmp = [a[:] for a in arr]

    for c in combi:
        x, y = c
        tmp[x][y] = 1
    
    q = deque()
    
    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 2:
                q.append([i, j])

                while q:
                    x, y = q.popleft()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx < N and 0 <= ny < M and tmp[nx][ny] == 0 and arr[nx][ny] == 0:
                            tmp[nx][ny] = 2
                            q.append([nx, ny])


    ans = sum(t.count(0) for t in tmp)
    answer = max(answer, ans)

print(answer)
# 벽을 꼭 3개를 세워야함 !! 