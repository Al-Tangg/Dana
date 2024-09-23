def dfs(node):
    visited[node] = 1

    for n in adj[node]:
        if visited[n] == 0:
            dfs(n)

N = int(input())
M = int(input())

adj = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split(' '))

    adj[a].append(b)
    adj[b].append(a)

dfs(1)

print(visited.count(1) - 1)

