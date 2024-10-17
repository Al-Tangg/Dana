import sys

def dfs(num, s_num, ans):
    visited[num] = 1
    path.append(num)

    if visited[arr[num]] == 0:
        dfs(arr[num], s_num, ans)
    elif arr[num] == s_num:
        ans += path[:]
        return

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    arr = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [0 for _ in range(N + 1)]

    ans = []

    for i in range(1, N+1):
        if visited[i] == 0:
            path = []
            dfs(i, i, ans)

    print(N-len(ans))