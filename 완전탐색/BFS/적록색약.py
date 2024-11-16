# https://www.acmicpc.net/problem/10026

import sys
from collections import deque

N = int(sys.stdin.readline().strip())
arr = []
arr2 = []

for _ in range(N):
    line = sys.stdin.readline()
    arr.append(list(line))
    line = line.replace('R', 'G')

    arr2.append(list(line))

q1 = deque()
visited1 = [[0 for _ in range(N)] for _ in range(N)]
ans1 = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(N):
    for j in range(N):
        if visited1[i][j] == 0:
            ans1 += 1
            q1.append([i, j, arr[i][j]])
            visited1[i][j] = 1

            while q1:
                x, y, color = q1.popleft()

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if 0 <= nx < N and 0 <= ny < N and visited1[nx][ny] == 0 and arr[nx][ny] == color:
                        q1.append([nx, ny, color])
                        visited1[nx][ny] = 1


q2 = deque()
visited2 = [[0 for _ in range(N)] for _ in range(N)]
ans2 = 0

for i in range(N):
    for j in range(N):
        if visited2[i][j] == 0:
            ans2 += 1
            q2.append([i, j, arr2[i][j]])
            visited2[i][j] = 1

            while q2:
                x, y, color = q2.popleft()

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if 0 <= nx < N and 0 <= ny < N and visited2[nx][ny] == 0 and arr2[nx][ny] == color:
                        q2.append([nx, ny, color])
                        visited2[nx][ny] = 1


print(ans1, ans2)


