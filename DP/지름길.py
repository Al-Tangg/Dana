# https://www.acmicpc.net/problem/1446

import sys
    
N, D = map(int, sys.stdin.readline().split())
jirum = []

for _ in range(N):
    jirum.append(list(map(int, sys.stdin.readline().split())))

dp = [sys.maxsize for _ in range(D + 1)]
dp[0] = 0

for i in range(1, D+1):
    dp[i] = min(dp[i-1] + 1, i)

    for ji in jirum:
        s, e, d = ji

        if i == e:
            dp[i] = min(dp[i], dp[s] + d)
print(dp[-1])
