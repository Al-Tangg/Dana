import sys
from collections import deque

while True:
    L, R, C = map(int, sys.stdin.readline().split()) # 층, 행, 열

    if L == R == C == 0:
        break

    arr = []
    visited = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(L)]

    for _ in range(L):
        l = []
        for _ in range(R):
            l.append(list(sys.stdin.readline().strip()))
        arr.append(l)

        sys.stdin.readline()

    q = deque()
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if arr[i][j][k] == 'S':
                    q.append([i, j, k, 0])
                    visited[i][j][k] = 1
                if arr[i][j][k] == 'E':
                    e_z, e_x, e_y = i, j, k  

    ans = "Trapped!"

    while q:
        z, x, y, t = q.popleft()

        if z == e_z and x == e_x and y == e_y:
            ans = "Escaped in " + str(t) + " minute(s)."
            break
        
        dz = [1, -1, 0, 0, 0, 0]
        dx = [0, 0, 1, -1, 0, 0]
        dy = [0, 0, 0, 0, 1, -1]

        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C and arr[nz][nx][ny] != '#' and visited[nz][nx][ny] == 0:
                q.append([nz, nx, ny, t + 1])
                visited[nz][nx][ny] = 1
    
    print(ans)

# .이 비어있는 칸임