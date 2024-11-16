# https://www.acmicpc.net/problem/1522

import sys

s = list(input())
A = s.count('a')
N = len(s)

s = s*2

l = 0
r = A

result = sys.maxsize

while l < N:
    result = min(result, s[l:r].count('b'))

    l += 1
    r += 1

print(result)