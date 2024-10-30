# https://www.acmicpc.net/problem/6593

import sys
from collections import deque

dz = [1, -1, 0, 0, 0, 0]
dx = [0 ,0, 1, -1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]

def bfs():
    while q:
        z, x, y, m = q.popleft()

        if arr[z][x][y] == 'E':
            return m

        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C and arr[nz][nx][ny] != '#' and visited[nz][nx][ny] == 0:
                q.append([nz, nx, ny, m + 1])
                visited[nz][nx][ny] = 1


while(True):
    # 층, 행, 열
    L, R, C = map(int, sys.stdin.readline().split())

    if L == R == C == 0:
        exit()
    
    arr = [] # 상범빌딩
    for _ in range(L):
        f = []
        for _ in range(R):
            f.append(list(sys.stdin.readline().strip()))
        
        arr.append(f)
        sys.stdin.readline()
    

    q = deque()
    visited = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(L)]

    for i in range(L):
        for j in range(R):
            for k in range(C):
                if arr[i][j][k] == 'S':
                    q.append([i, j, k, 0])
                    visited[i][j][k] = 1
                    
                    result = bfs()

                    if result:
                        print("Escaped in %d minute(s)." %result)
                    else:
                        print("Trapped!")

