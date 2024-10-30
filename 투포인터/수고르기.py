# https://www.acmicpc.net/problem/2230

import sys

N, M = map(int, sys.stdin.readline().split())
arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline().strip()))

arr.sort()

result = sys.maxsize

l = 0
r = 0

while l <= r and r < N:
    while l <= r and arr[r] - arr[l] >= M:
        if result > arr[r] - arr[l]:
            result = arr[r] - arr[l]
        l += 1
    
    r += 1

print(result)