# https://www.acmicpc.net/problem/1018

import sys

N, M = map(int, sys.stdin.readline().split())
arr = []

answer = sys.maxsize

for _ in range(N):
    arr.append(sys.stdin.readline().strip())

chess = ["WBWBWBWB",
         "BWBWBWBW",
         "WBWBWBWB",
         "BWBWBWBW",
         "WBWBWBWB",
         "BWBWBWBW",
         "WBWBWBWB",
         "BWBWBWBW"]

for i in range(N-7):
    for j in range(M-7):

        cnt = 0

        for r in range(8):
            for c in range(8):
                if chess[r][c] == arr[i+r][j+c]:
                    cnt += 1
        
        answer = min(answer, cnt, 64 - cnt)

print(answer)



        
        

# 이 보드를 잘라서 8×8 크기의 체스판