import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

dp = [sys.maxsize for _ in range(100001)]

q = deque()
q.append([N, 0])
dp[N] = 0

while q:
    now, t = q.popleft()

    if now - 1 >= 0 and dp[now - 1] > t + 1:
        dp[now - 1] = t + 1
        q.append([now - 1, t + 1])
    if now + 1 <= 100000 and dp[now + 1] > t + 1:
        dp[now + 1] = t + 1
        q.append([now + 1, t  + 1])
    if now * 2 <= 100000 and dp[now*2] > t:
        dp[now*2]  = t
        q.append([now*2, t])

print(dp[K])