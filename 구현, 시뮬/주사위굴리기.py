# https://www.acmicpc.net/problem/14499

import sys

N, M, x, y, K = map(int, sys.stdin.readline().split()) # 지도 세로, 가로, 주사위 좌표, 명령 개수
map_arr = []

for _ in range(N):
    map_arr.append(list(map(int, sys.stdin.readline().split())))
commands = list(map(int, sys.stdin.readline().split()))

dice = [0, 0, 0, 0, 0, 0]

# 우 좌 상 하
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for com in commands:
    nx = x + dx[com-1]
    ny = y + dy[com-1]

    if 0 <= nx < N and 0 <= ny < M:
        x, y = nx, ny

        if com == 1:
            dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[2] 
        elif com == 2:
            dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3] 
        elif com == 3:
            dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]
        elif com == 4:
            dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]
    

        if map_arr[x][y] == 0:
            map_arr[x][y] = dice[5]
        else:
            dice[5] = map_arr[x][y]
            map_arr[x][y] = 0
        
        print(dice[0])
