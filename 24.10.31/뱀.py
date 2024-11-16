import sys
from collections import deque

N = int(sys.stdin.readline().strip())
K = int(sys.stdin.readline().strip())

arr = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(K):
    x, y = map(int, sys.stdin.readline().split())

    arr[x-1][y-1] = 1

L = int(sys.stdin.readline().strip())
directions = []

for _ in range(L):
    directions.append(list(sys.stdin.readline().split()))


q = deque()
q.append([0, 0])

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

t = 0
d = 1

while True:
    t += 1

    x, y = q[-1]

    nx, ny = x + dx[d], y + dy[d]

    if nx < 0 or nx >= N or ny < 0 or ny >= N or [nx, ny] in q:
        print(t)
        break

    q.append([nx, ny])

    if arr[nx][ny] == 1:
        arr[nx][ny] = 0
    else:
        q.popleft()
    
    for di in directions:
        X, C = di

        if t == int(X):
            if C == 'L':
                if d == 0:
                    d = 3
                else:
                    d -= 1
            elif C == 'D':
                d = (d+1) % 4