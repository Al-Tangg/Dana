# https://www.acmicpc.net/problem/21610

import sys

N, M = map(int, sys.stdin.readline().split())
arr = []

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
groom = [[0 for _ in range(N)] for _ in range(N)]

groom[N-1][0], groom[N-1][1], groom[N-2][0], groom[N-2][1] = 1, 1, 1, 1

for m in range(M):
    d, s = map(int, sys.stdin.readline().split())

    tmp = [[0 for _ in range(N)] for _ in range(N)]

    # step 1, 2
    for i in range(N):
        for j in range(N):
            if groom[i][j] == 1:
                nx = (i + dx[d-1] * s) % N
                ny = (j + dy[d-1] * s) % N
                arr[nx][ny] += 1
                tmp[nx][ny] = 1
    
    for i in range(N):
        for j in range(N):
            if tmp[i][j] == 1:
                for k in range(4):
                    nx = i + dx[2*k - 1]
                    ny = j + dy[2*k - 1]

                    if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] > 0:
                        arr[i][j] += 1
    
    for i in range(N):
        for j in range(N):
            if tmp[i][j] == 1:
                tmp[i][j] = 0
            elif arr[i][j] >= 2:
                arr[i][j] -= 2
                tmp[i][j] = 1
    
    groom = tmp

print(sum(sum(a) for a in arr))
    

                
    