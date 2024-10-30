# https://www.acmicpc.net/problem/2467

import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

result = (1000000000, 1000000000)

l = 0
r = N - 1

while l < r:
    value = arr[r] + arr[l]

    if abs(value) < abs(result[1] + result[0]):
        result = (arr[l], arr[r])

    if value < 0:
        l += 1
    elif value > 0:
        r -= 1
    else:
        print(arr[l], arr[r])
        exit()
    
print(result[0], result[1])