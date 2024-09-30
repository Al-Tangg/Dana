N = int(input())
arr = list(map(int, input().split()))

n = [i for i in arr]

for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i]:
            n[i] = max(n[i], n[j] + arr[i])

print(max(n))