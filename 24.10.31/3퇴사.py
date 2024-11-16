import sys

N = int(sys.stdin.readline().strip())
arr = []

dp = [0 for _ in range(N+1)]

for i in range(1, N + 1):
    T, P = map(int, sys.stdin.readline().split())
    arr.append([i + T - 1, P]) # 작업이 끝나는 시간을 저장

for i in range(1, N + 1):
    if arr[i - 1][0] <= N: # 퇴사일보다 빨리 끝나는 것만 계산
        dp[i] = max(dp[i], arr[i-1][1])
    
        for j in range(1, N + 1):
            if arr[j-1][0] < i: # 내가 작업을 시작하는 날보다 작업이 빨리 끝나는 작업을 대상으로
                dp[i] = max(dp[i], dp[j] + arr[i-1][1])

print(max(dp))

