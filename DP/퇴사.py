# https://www.acmicpc.net/problem/14501

import sys

N = int(sys.stdin.readline().strip())
arr = []

for i in range(N):
    T, P = map(int, sys.stdin.readline().split())

    arr.append([i + T, P])

dp = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    if arr[i-1][0] > N:
        continue

    dp[i] = max(dp[i], arr[i-1][1])

    for j in range(1, i + 1):
        if arr[j-1][0] < i:
            dp[i] = max(dp[i], dp[j] + arr[i-1][1])
            
print(max(dp))

