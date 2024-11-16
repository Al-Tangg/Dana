import sys

N, M = map(int, sys.stdin.readline().split())
arr = [] 

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))


cloud = [[0 for _ in range(N)] for _ in range(N)]
cloud[N-1][0], cloud[N-1][1], cloud[N-2][0], cloud[N-2][1] = 1, 1, 1, 1

# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

for _ in range(M):
    d, s = map(int, sys.stdin.readline().split())

    tmp = [[0 for _ in range(N)] for _ in range(N)]

    # 구름 이동
    for i in range(N):
        for j in range(N):
            if cloud[i][j] == 1:
                x, y = (i + dx[d-1] * s) % N, (j + dy[d-1] * s) % N
                tmp[x][y] = 1
                arr[x][y] += 1
    
    # 비바라기 마법
    for i in range(N):
        for j in range(N):
            if tmp[i][j] == 1:
                for k in range(4):
                    x, y = i + dx[2*k-1], j + dy[2*k-1]

                    if 0 <= x < N and 0 <= y < N and arr[x][y] > 0:
                        arr[i][j] += 1    
    
    # step 5
    for i in range(N):
        for j in range(N):
            if tmp[i][j] == 1:
                tmp[i][j] = 0
            elif arr[i][j] >= 2:
                arr[i][j] -= 2
                tmp[i][j] = 1
    
    cloud = tmp
                
    
print(sum(sum(a) for a in arr))