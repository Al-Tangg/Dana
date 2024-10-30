import sys

N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    arr[i][0] += i

dp = [0 for x in arr]

print(arr)
print(dp)


