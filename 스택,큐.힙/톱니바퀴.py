# https://www.acmicpc.net/problem/14891

import sys
from collections import deque

arr = []

for _ in range(4):
    q = deque(list(map(int, list(sys.stdin.readline().strip()))))
    arr.append(q)

K = int(sys.stdin.readline())

def rotation(d, num):
    if d == 1:
        arr[num].appendleft(arr[num].pop())
    else:
        arr[num].append(arr[num].popleft())

for _ in range(K):
    num, d = map(int, sys.stdin.readline().split())

    flag_l = num - 2 >= 0 and arr[num-1][-2] != arr[num-2][2]
    flag_r = num < 4 and arr[num-1][2] != arr[num][-2]

    tmp_r, r_d = num, d
    while tmp_r < 4 and flag_r:
        flag_r = tmp_r + 1 < 4 and arr[tmp_r][2] != arr[tmp_r + 1][-2]
        rotation(-r_d, tmp_r)
        tmp_r += 1
        r_d = -r_d
    
    tmp_l, l_d = num, d
    while tmp_l - 2 >= 0 and flag_l:
        flag_l = tmp_l - 3 >= 0 and arr[tmp_l-2][-2] != arr[tmp_l-3][2]
        rotation(-l_d, tmp_l-2)
        tmp_l -= 1
        l_d = -l_d
    
    rotation(d, num-1)

    
result = 0

if arr[0][0] == 1:
    result += 1
if arr[1][0] == 1:
    result += 2
if arr[2][0] == 1:
    result += 4
if arr[3][0] == 1:
    result += 8

print(result)
