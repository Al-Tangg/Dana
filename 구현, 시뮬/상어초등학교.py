# https://www.acmicpc.net/problem/21608

import sys

N = int(sys.stdin.readline())
arr = [[0 for _ in range(N)] for _ in range(N)] # 좌석 배치도
stu_prefers = [[] for _ in range(N**2+1)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(N**2):
    stu, a, b, c, d = map(int, sys.stdin.readline().split())
    prefers = [a, b, c, d]
    stu_prefers[stu].append(prefers)

    seats = [] # 가능한 좌석들

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                like = 0
                empty = 0

                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0 <= nx < N and 0 <= ny < N:
                        if arr[nx][ny] in prefers:
                            like += 1
                        elif arr[nx][ny] == 0:
                            empty += 1

                seats.append([i, j, like, empty])

    seats.sort(key = lambda x: (-x[2], -x[3], x[0], x[1]))

    x, y = seats[0][0], seats[0][1]
    arr[x][y] = stu

result = 0
for i in range(N):
    for j in range(N):
        cnt = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] in stu_prefers[arr[i][j]][0]:
                cnt += 1
        if cnt > 0:
            result += (10**(cnt-1))
        
print(result)