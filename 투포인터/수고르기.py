import sys

N, M = map(int, sys.stdin.readline().split())
arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline().strip()))

arr.sort()

l = 0
r = 0

answer = sys.maxsize

# 그 차이가 M 이상이면서 가장 작은 경우

while l <= r and r < N:
    val = arr[r] - arr[l] 
    if val >= M:
        if val < answer:
            answer = val
        l += 1
    else:
        r += 1

print(answer)

# 이 방식은 하나만찾게 되네