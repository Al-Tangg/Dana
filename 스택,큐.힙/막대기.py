# https://www.acmicpc.net/problem/1094

import heapq

X = int(input())
mak = [64]

while sum(mak) != X:
    s = heapq.heappop(mak)

    if sum(mak) + s // 2 < X:
        heapq.heappush(mak, s / 2)

    heapq.heappush(mak, s / 2)

print(len(mak))