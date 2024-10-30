# https://www.acmicpc.net/problem/1522

from collections import deque

s = list(input())
A = s.count('a')
N = len(s)

for i in range(N):
    ss = s[i]
    if ss == 'a':
        q = deque()
        visited = [0 for _ in range(N)]

        q.append(i, s)
        visited[i] = 1

        while q:
            idx, w = q.popleft()

            for j in range(idx + 1, N):
                if visited[j] == 0 and s[j] == 'b':
                    tmp = s
                    tmp[idx], tmp[j] = tmp[j], tmp[idx]

                    q.append()


