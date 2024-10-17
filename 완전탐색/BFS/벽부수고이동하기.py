import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
arr = []

for _ in range(N):
    arr.append(list(sys.stdin.readline().strip()))

q = deque()
visited = [[0 for _ in range(M)] for _ in range(N)]
q.append([0, 0, 0, 0])
visited[0][0] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = - 1

while q:
    x, y, flag, cnt = q.popleft()

    if x == N - 1 and y == M - 1:
        answer = cnt + 1
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if flag == 0:
                q.append([nx, ny, 1, cnt + 1])
            elif visited[nx][ny] == 0 and arr[nx][ny] == '0':
                q.append([nx, ny, flag, cnt + 1])

print(answer)