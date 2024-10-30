# https://www.acmicpc.net/problem/1806

import sys

N, S = map(int, sys.stdin.readline().split())
arr = [0] + list(map(int, sys.stdin.readline().split()))

s = [0 for _ in range(N+1)]

for i in range(N+1):
    s[i] = s[i-1] + arr[i]

l = 1
r = 1

result = (0, sys.maxsize)

while r < N + 1:
    while s[r] - s[l-1] >= S:
        if result[1] - result[0] > r - l:
            result = (l, r)
        l += 1
        
    r += 1

print(result[1] - result[0] + 1 if result[1] - result[0] != sys.maxsize else 0)