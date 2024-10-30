# https://www.acmicpc.net/problem/14940

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

answer = [[sys.maxsize for _ in range(m)] for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:

            q = deque()
            q.append([0, 0, 0])
            answer[i][j] = 0

            while q:
                x, y, cnt = q.popleft()

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1 and answer[nx][ny] > cnt + 1:
                        answer[nx][ny] = cnt + 1
                        q.append([nx, ny, cnt + 1])


for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            answer[i][j] = '0'
        else:
            if answer[i][j] == sys.maxsize:
                answer[i][j] = '-1'
            else:
                answer[i][j] = str(answer[i][j])

for ans in answer:
    print(' '.join(ans))