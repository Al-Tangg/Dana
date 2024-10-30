# https://www.acmicpc.net/problem/16928

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split()) # 사다리 수, 뱀 수
info = [0 for _ in range(101)]

visited = [0 for _ in range(101)]

for _ in range(N + M):
    s, e = map(int, sys.stdin.readline().split())
    info[s] = e

q = deque()
q.append([1, 0])
visited[1] = 1

while True:
    now, cnt = q.popleft()

    if now == 100:
        print(cnt)
        break

    for i in range(1, 7):
        next = now + i

        if next <= 100 and visited[next] == 0:
            if info[next] == 0:
                q.append([next, cnt + 1])
                visited[next] = 1
            elif visited[info[next]] == 0:
                q.append([info[next], cnt + 1])
                visited[info[next]] = 1