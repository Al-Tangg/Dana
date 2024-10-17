# https://www.acmicpc.net/problem/2468

import sys
from collections import deque

N = int(sys.stdin.readline())
arr = []
hs = set() # 높이들

for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    arr.append(row)
    hs.update(row)

answer = 1
dx = [1, -1 ,0 ,0]
dy = [0, 0, 1, -1]

for h in hs:
    q = deque()
    visited = [[0 for _ in range(N)] for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] > h and visited[i][j] == 0:
                cnt += 1
                q.append([i, j])
                visited[i][j] = 1

                while q:
                    x, y = q.popleft()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] > h and visited[nx][ny] == 0:
                            q.append([nx, ny])
                            visited[nx][ny] = 1

    if cnt > answer:
        answer = cnt

print(answer)
