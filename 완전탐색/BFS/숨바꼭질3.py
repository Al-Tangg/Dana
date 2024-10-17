import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split()) # 수빈, 동생

# 항상 x+1, x-1, 순간 이동 하는 선택을 할 수 있음
q = deque()
dp = [sys.maxsize for _ in range(100001)] # 걸린 시간

q.append([N, 0])
dp[N] = 0

while q:
    x, t= q.popleft()

    if 2*x <= 100000 and t < dp[2*x]:
        q.append([2*x, t])
        dp[2*x] = t
    if x + 1 <= 100000 and t + 1 < dp[x+1]:
        q.append([x+1, t+1])
        dp[x+1] = t + 1
    if x - 1 >= 0 and t + 1 < dp[x-1]:
        q.append([x-1, t+1])
        dp[x-1] = t + 1
    
print(dp[M])