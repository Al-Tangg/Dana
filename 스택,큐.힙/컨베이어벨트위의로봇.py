# https://www.acmicpc.net/problem/20055

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split())) # 각 칸의 현재 내구도

belts = deque(arr)
robots = deque([False] * N, maxlen = N)

answer = 0

while belts.count(0) < K:
    # step1 회전
    belts.rotate(1)
    robots.rotate(1)

    # 로봇이 내릴 위치에 오면 즉시 내리기
    robots[-1] = False

    # step2 가장 먼저 벨트에 올라간 로봇부터 처리
    for i in range(N-1, -1, -1):
        if robots[i] and not robots[i+1] and belts[i+1] > 0:
            belts[i+1] -= 1
            robots[i] = False
            robots[i+1] = True
    
    # 로봇이 내릴 위치에 오면 즉시 내리기
    robots[-1] = False

    # step3
    if belts[0] > 0:
        belts[0] -= 1
        robots[0] = True
    
    answer += 1

print(answer)