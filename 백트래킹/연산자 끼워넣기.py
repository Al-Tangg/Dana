# https://www.acmicpc.net/problem/14888

import sys

# 수열 index, 연산자 idx, 지금까지의 연산 결과
def dfs(idx, op, value):
    global max_num, min_num

    ops[op] -= 1

    if op == 0:
        value += arr[idx]
    elif op == 1:
        value -= arr[idx]
    elif op == 2:
        value *= arr[idx]
    elif op == 3:
        if value > 0:
            value //= arr[idx]
        else:
            value = -(abs(value) // arr[idx])
    
    if idx == len(arr) - 1:
        max_num = max(max_num, value)
        min_num = min(min_num, value)
        return

    for i in range(4):
        if ops[i] > 0:
            dfs(idx + 1, i, value)
            ops[i] += 1

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split())) # 수열
ops = list(map(int, sys.stdin.readline().split())) # +, -, *, // 수

# 모든 연산 결과가 마이너스일 수도 있음 !!!!! 
max_num = -sys.maxsize
min_num = sys.maxsize

for i in range(4):
    if ops[i] > 0:
        dfs(1, i, arr[0])
        ops[i] += 1

print(max_num)
print(min_num)
            