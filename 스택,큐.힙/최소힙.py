import sys
import heapq

N = int(sys.stdin.readline().strip())
arr = []

for _ in range(N):
    n = int(sys.stdin.readline().strip())

    if n == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(heapq.heappop(arr))
    else:
        heapq.heappush(arr, n)