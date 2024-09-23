# 정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸
from collections import deque
from sys import stdin

M, N, H = map(int, stdin.readline().split(' '))

tomato = []

for _ in range(N*H):
    tomato.append(list(map(int, stdin.readline().split(' '))))

q = deque()

for i in range(len(tomato)):
    for j in range(M):
        if tomato[i][j] == 1:
            q.append([i, j, 0])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    i, j, cnt = q.popleft()
    layer = i // N # 현재 층
    h  = i % N # 층 내의 행

    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]

        if layer *N <= nx < (layer+1) * N and 0<= ny < M:
            if tomato[nx][ny] == 0:
                tomato[nx][ny] = 1
                q.append([nx, ny, cnt+1])

    if layer > 0:
        x = N*(layer-1) + h
        if tomato[x][j] == 0:
            tomato[x][j] = 1
            q.append([x, j, cnt+1])
    
    if layer < H -1:
        x = N*(layer+1) + h
        if tomato[x][j] == 0:
            tomato[x][j] = 1
            q.append([x, j, cnt+1])


for i in range(len(tomato)):
    for j in range(M):
        if tomato[i][j] == 0:
            print(-1)
            exit()

print(cnt)