# https://www.acmicpc.net/problem/14889

import sys

answer = sys.maxsize

def dfs(num, cnt):
    global N, answer
    visited[num] = 1

    if cnt == N // 2:
        start = 0
        link = 0

        for i in range(N):
            for j in range(N):
                if visited[i] == 1 and visited[j] == 1:
                    start += arr[i][j]
                elif visited[i] == 0 and visited[j] == 0:
                    link += arr[i][j]
        
        answer = min(answer, abs(start - link))
        return
    
    else:
        for i in range(num + 1, N):
            if visited[i] == 0:
                dfs(i, cnt + 1)
                visited[i] = 0


N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

visited = [0 for _ in range(N)]
dfs(0, 1)

print(answer)