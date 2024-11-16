# https://www.acmicpc.net/problem/5427

import sys
from collections import deque

T = int(sys.stdin.readline().strip())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# . 빈 공간, # 뱍, @ 상근이 시작 위치, * 불
for _ in range(T):
    answer = "IMPOSSIBLE"
    w, h = map(int, sys.stdin.readline().split())
    arr = []

    for _ in range(h):
        arr.append(list(sys.stdin.readline().strip()))
    
    f_q = deque() # 블 이동
    s_q = deque() # 상근 이동
    visited = [[0 for _ in range(w)] for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if arr[i][j] == '*':
                f_q.append([i, j, 1])
                visited[i][j] = 1
            elif arr[i][j] == '@':
                s_q.append([i, j, 1])
                visited[i][j] = -1 # 방문 처리 
    
    while f_q:
        x, y, cnt = f_q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] != '#' and visited[nx][ny] <= 0:
                f_q.append([nx, ny, cnt + 1])
                visited[nx][ny] = cnt + 1

    while s_q:
        x, y, cnt = s_q.popleft()

        if x == 0 or x == h - 1 or y == 0 or y == w - 1:
            answer = cnt
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == '.' and (visited[nx][ny] > cnt + 1 or visited[nx][ny] == 0):
                s_q.append([nx, ny, cnt + 1])
                visited[nx][ny] = -1
    
    print(answer)