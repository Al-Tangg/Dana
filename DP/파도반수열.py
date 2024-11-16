# https://www.acmicpc.net/problem/9461

import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    N = int(sys.stdin.readline().strip())

    dp = [0 for _ in range(101)]
    dp[1], dp[2], dp[3], dp[4], dp[5], dp[6], dp[7], dp[8], dp[9]  = 1, 1, 1, 2, 2, 3, 4, 5, 7

    for i in range(10, N + 1):
        dp[i] = dp[i-1] + dp[i-5]
    
    print(dp[N])