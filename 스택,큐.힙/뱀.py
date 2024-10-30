# https://www.acmicpc.net/problem/3190

import sys
from collections import deque

N = int(sys.stdin.readline().strip())
K = int(sys.stdin.readline().strip()) # 사과 개수
board = [[0 for _ in range(N)] for _ in range(N)] # 보드판, 1은 사과

for _ in range(K):
    x, y = map(int, sys.stdin.readline().split())

    board[x-1][y-1] = 1

L = int(sys.stdin.readline().strip()) # 방향 전환 정보
directions = []

for _ in range(L):
    directions.append(list(sys.stdin.readline().split()))

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

t = 0
d = 1

q = deque()
q.append([0, 0])

while True:
    t += 1
    
    x, y = q[-1]

    # 다음 머리 위치
    nx = x + dx[d]
    ny = y + dy[d]

    # 종료 조건: 벽을 만나거나 자기 자신한테 부딪히거나
    if nx < 0 or nx >= N or ny < 0 or ny >= N or [nx, ny] in q:
        print(t)
        break

    q.append([nx, ny])

    if board[nx][ny] == 1: # 사과가 있다면
        board[nx][ny] = 0
    else:
        q.popleft()

    for di in directions:
        X, C = di

        if t == int(X):
            if C == 'L':
                if d == 0:
                    d = 3
                else:
                    d -= 1
            elif C == 'D':
                d = (d+1) % 4
    