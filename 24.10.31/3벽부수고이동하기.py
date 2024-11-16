import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
arr = []

for _ in range(N):
    arr.append(list(map(int, list(sys.stdin.readline().strip()))))

visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
# 0은 벽을 아직 안 부순 경로, 1은 벽을 부순 경로

q = deque()
q.append([0, 0, 0, 1]) # x, y, flag, cnt
visited[0][0][0] = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    x, y, flag, cnt = q.popleft()

    if x == N - 1 and y == M - 1:
         print(cnt)
         exit()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny][flag] == 0:
            if arr[nx][ny] == 0:
                q.append([nx, ny, flag, cnt + 1])
                visited[nx][ny][flag] = 1
            elif flag == 0: # 벽을 뚫는 경우
                q.append([nx, ny, 1, cnt + 1])
                visited[nx][ny][1] = 1
                
print(-1)
