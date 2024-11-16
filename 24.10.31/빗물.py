import sys

H, W = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

answer = 0

for i in range(1, W-1):
    answer += max((min(max(arr[:i]), max(arr[i+1:]))) - arr[i], 0)

print(answer)