# https://www.acmicpc.net/problem/16113

import sys

N = int(sys.stdin.readline())
signal = sys.stdin.readline()
arr = []

C = N//5

for i in range(5):
    arr.append(list(signal[i*C: i*C + C]))

digit = [[0, 1], [1, 0], [1, 2], [2, 1], [3, 0], [3, 2], [4, 1]]
nums = [[0, 1, 2, 4, 5, 6],
        [1, 4],
        [0, 2, 3, 4, 6],
        [0, 2, 3, 5, 6],
        [1, 2, 3, 5],
        [0, 1, 3, 5, 6],
        [0, 1, 3, 4, 5, 6],
        [0, 2, 5],
        [0, 1, 2, 3, 4, 5, 6],
        [0, 1, 2, 3, 5, 6]]

c = 0
while c < C:
    ans = []

    cols = 0
    for i in range(5):
        if arr[i][c] == '.':
            cols += 0
        else:
            cols += 1

    if cols == 0:
        c += 1
        continue

    if cols == 5:
        sec_cols = 0
        if c == C - 1:
            print(1, end = "")
        else:
            for i in range(5):
                if arr[i][c+1] == '#':
                    sec_cols += 1
            if sec_cols == 0:
                print(1, end = "")
                c += 1
                continue
    
    if c < C-2:
        for k in range(len(digit)):
            x, y = digit[k]
            if arr[x][c+y] == '#':
                ans.append(k)

        for i in range(10):
            if nums[i] == ans:
                print(i, end = "")
        c += 3  
    else:
        c +=1    