import sys

N, S = map(int, sys.stdin.readline().split())
arr = [0] + list(map(int, sys.stdin.readline().split()))

s = [0 for _ in range(N+1)]
for i in range(1,N+1):
    s[i] = s[i-1] + arr[i]

l = 1
r = 1

answer = sys.maxsize

while l <= r and r <= N :
    while s[r] - s[l-1] >= S:
        if answer > r - l + 1:
            answer = r - l + 1
        l += 1
    else:
        r += 1
    
print(answer if answer != sys.maxsize else 0)