import sys
from collections import deque

N, L, R = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = 0

def bfs(x, y):
    q.append([x, y])
    path.append([x, y])
    person = arr[x][y]
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
                    
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N and L <= abs(arr[x][y] - arr[nx][ny]) <= R and visited[nx][ny] == 0:
                q.append([nx, ny])
                path.append([nx, ny])
                person += arr[nx][ny]
                visited[nx][ny] = 1
        
    if len(path) > 1:
        person = person // len(path)
        for p in path:
            x, y = p
            arr[x][y] = person
    
    return len(path) > 1

while True:
    flag = 1
    q = deque()
    visited = [[0 for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                path = []

                if bfs(i, j) == True:
                    flag = 0
    
    if  flag == 1:
        print(answer)
        exit()
    else:
        answer += 1