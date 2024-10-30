# https://www.acmicpc.net/problem/14500

import sys

N, M = map(int, sys.stdin.readline().split())
arr = []

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

result = 0

type = [[[1, 1, 1, 1]],[[1], [1], [1], [1]],
        [[1, 1],
         [1, 1]],
         [[1,1],[1,0],[1,0]], [[1,1], [0, 1], [0,1]], [[1, 0],[1, 0], [1, 1]], [[0, 1], [0, 1], [1, 1]],
         [[1, 0, 0], [1, 1, 1]], [[0, 0, 1], [1, 1, 1]], [[1, 1, 1], [1, 0, 0]], [[1, 1, 1,], [0, 0, 1]],
         [[1, 0], [1, 1], [0, 1]], [[0, 1], [1, 1], [1, 0]], [[1, 1, 0], [0, 1, 1]], [[0, 1, 1], [1, 1, 0]],
         [[0, 1, 0], [1, 1, 1]], [[1, 1, 1], [0, 1, 0]], [[1, 0], [1, 1], [1, 0]], [[0, 1], [1, 1], [0, 1]]]

for t in type:
    r = len(t)
    c = len(t[0])

    for i in range(N - r + 1):
        for j in range(M - c + 1):
            ans = 0
            for k in range(r):
                for l in range(c):
                    if t[k][l] == 1:
                        ans += arr[i+k][j+l]
            
            if ans > result:
                result = ans

print(result)