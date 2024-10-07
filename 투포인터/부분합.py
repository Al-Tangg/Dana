import sys

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
result = 100001

# 부분합
s = [0 for _ in range(N+1)]
s[1] = arr[0]

for i in range(2, N+1):
    s[i] = s[i-1] + arr[i-1]

l = 1
r = 1

while l <= r and r < N + 1:
    while s[r] - s[l-1] >= S:
        if result > r - l:
            result = r - (l - 1)
        l += 1
    
    r += 1

print(result if result < 100001 else 0)