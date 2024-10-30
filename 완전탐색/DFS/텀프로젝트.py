# https://www.acmicpc.net/problem/9466

import sys
sys.setrecursionlimit(10 ** 6)

def dfs(num):
    global teams
    
    visited[num] = 1
    cycle.append(num)

    value = arr[num]

    if visited[value]:
        if value in cycle:
            teams += cycle[cycle.index(value):]
            return
    else:
        dfs(value)

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    arr = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [0 for _ in range(N+1)]

    teams = []

    for i in range(1, N+1):
        if visited[i] == 0:
            cycle = []
            dfs(i)

    print(N - len(teams))