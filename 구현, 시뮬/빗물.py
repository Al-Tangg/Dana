# https://www.acmicpc.net/problem/14719

import sys

H, W = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

result = 0

for i in range(1, W):
    result += max((min(max(arr[:i]), max(arr[i:])) - arr[i]), 0)

print(result)