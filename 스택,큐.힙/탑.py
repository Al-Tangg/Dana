# https://www.acmicpc.net/problem/2493

import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

result = ['0' for _ in range(N)]

s = [0]

for i in range(1, N):
    while len(s) > 0 and arr[s[-1]] < arr[i]:
        s.pop()
    
    if len(s) != 0:
        result[i] = str(s[-1] + 1)
    
    s.append(i)

print(' '.join(result))
