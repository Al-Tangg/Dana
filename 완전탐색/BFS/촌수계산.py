from collections import deque

n = int(input())
c, d = map(int, input().split(' '))
m = int(input())

arr = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split(' '))
    arr[a].append(b)
    arr[b].append(a)

q = deque()
q.append([c, 0])

while q:
    node, cnt = q.popleft()
    visited[node] = 1

    if node == d:
        print(cnt)
        exit(0)

    for n in arr[node]:
        if visited[n] == 0:
            q.append([n, cnt+1])

print(-1)