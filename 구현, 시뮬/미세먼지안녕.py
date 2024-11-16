# https://www.acmicpc.net/problem/17144

import sys

R, C, T = map(int, sys.stdin.readline().split())
arr = []

for _ in range(R):
    arr.append(list(map(int, sys.stdin.readline().split())))

air = []

for i in range(R):
    if arr[i][0] == -1:
        air.append(i)
    
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(T):
    tmp = [a[:] for a in arr]

    # 미세먼지 확산
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                a = arr[i][j] // 5
            
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] >= 0:
                        tmp[nx][ny] += a
                        tmp[i][j] -= a

    arr = tmp

    # 공기청정기 순환(반시계)
    for i in range(air[0]-1, 0, -1):
        arr[i][0] = arr[i-1][0]

    for i in range(C-1):
        arr[0][i] = arr[0][i+1]

    for i in range(air[0]):
        arr[i][C-1] = arr[i+1][C-1]
    
    for i in range(C-1, 1, -1):
        arr[air[0]][i] = arr[air[0]][i-1]
    
    arr[air[0]][1] = 0

    # 공기청정기 순환(시계)
    for i in range(air[1] + 1, R - 1, 1):
        arr[i][0] = arr[i+1][0]
    
    for i in range(C-1):
        arr[R-1][i] = arr[R-1][i+1]
    
    for i in range(R-1, air[1], -1):
        arr[i][C-1] = arr[i-1][C-1]

    for i in range(C-1, 1, -1):
        arr[air[1]][i] = arr[air[1]][i-1]
    
    arr[air[1]][1] = 0

result = 0

for a in arr:
    for aa in a:
        if aa > 0:
            result += aa

print(result)