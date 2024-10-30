# https://www.acmicpc.net/problem/16987

import sys

answer = 0

def dfs(idx, cnt):
    global N, answer

    if idx == N :
        if answer < cnt:
            answer = cnt
        return
    
    flag = True

    for i in range(N):
        if i != idx and arr[i][0] > 0 and arr[idx][0] > 0:
            flag = False
            arr[idx][0] -= arr[i][1]
            arr[i][0] -= arr[idx][1]

            tmp = 0

            if arr[idx][0] <= 0:
                tmp += 1
            if arr[i][0] <= 0:
                tmp += 1
            
            dfs(idx + 1, cnt + tmp)

            arr[idx][0] += arr[i][1]
            arr[i][0] += arr[idx][1]
    
    if flag:
        dfs(idx + 1, cnt)


N = int(sys.stdin.readline()) # 계란의 수
arr = [] # 계란 내구도, 무게

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

dfs(0, 0)

print(answer)