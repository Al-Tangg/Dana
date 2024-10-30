# https://www.acmicpc.net/problem/2206

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
arr = []

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().strip())))

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

q = deque()
q.append([0, 0, 0]) # i, j, flag
visited[0][0][0] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    x, y, flag = q.popleft()

    if x == N - 1 and y == M - 1:
        print(visited[x][y][flag])
        exit()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] == 0 and visited[nx][ny][flag] == 0:
                q.append([nx, ny, flag])
                visited[nx][ny][flag] = visited[x][y][flag] + 1
            elif flag == 0 and arr[nx][ny] == 1: # 벽 부수기 !!
                q.append([nx, ny, 1])
                visited[nx][ny][1] = visited[x][y][0] + 1

print(-1)