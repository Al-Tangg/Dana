import sys

N, M, x, y, K = map(int, sys.stdin.readline().split())

arr = []

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

directions = list(map(int, sys.stdin.readline().split()))

dice = [0, 0, 0, 0, 0, 0]

# 동 서 북 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for d in directions:    
    nx, ny = x + dx[d-1], y + dy[d-1]

    if 0 <= nx < N and 0 <= ny < M:
        x, y = nx, ny

        if d == 1:
            dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]
        elif d == 2:
            dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]
        elif d == 3:
            dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]
        elif d == 4:
            dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]
        
        if arr[x][y] == 0:
            arr[x][y] = dice[5]
        else:
            dice[5] = arr[nx][ny]
            arr[x][y] = 0
        
        print(dice[0])