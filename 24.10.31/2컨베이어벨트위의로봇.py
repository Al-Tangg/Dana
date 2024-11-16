import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

belts = deque(arr)
robots = deque([0 for _ in range(N)], maxlen = N)

cnt = 0

while belts.count(0) < K:
    cnt += 1
    # step 1
    belts.rotate(1)
    robots.rotate(1)

    robots[-1] = 0

    # step2
    for i in range(N - 2, -1, -1):
        if robots[i] == 1 and robots[i+1] == 0 and belts[i+1] > 0:
            robots[i], robots[i+1] = robots[i+1], robots[i]
            belts[i+1] -= 1
    
    robots[-1] = 0
    
    # step3
    if belts[0] > 0:
        belts[0] -= 1
        robots[0] = 1

print(cnt)