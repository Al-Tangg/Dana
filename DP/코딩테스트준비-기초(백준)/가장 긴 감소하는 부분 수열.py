# 1. 작은 문제를 합쳐서 큰 문제를 해결할 수 있어야하고
# 2. 반복되는 문제가 있어야 한다.

N = int(input())
arr = list(map(int, input().split()))

n = [1 for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        if arr[i] < arr[j]:
            n[i] = max(n[i], n[j] + 1)

print(max(n))