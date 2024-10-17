import sys

H, W = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
answer = 0

for i in range(1, W-1):
    l_max = max(arr[:i])
    r_max = max(arr[i+1:])

    answer += (max(arr[i], min(l_max, r_max)) - arr[i])


print(answer)