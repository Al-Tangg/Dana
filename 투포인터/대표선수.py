import sys

N, M = map(int, sys.stdin.readline().split())
arr = []

for _ in range(N):
    stus = list(map(int, sys.stdin.readline().split()))
    stus.sort()
    arr.append(stus)

print(arr)