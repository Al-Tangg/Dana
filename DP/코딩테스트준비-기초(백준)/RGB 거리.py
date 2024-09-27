# 1. 작은 문제를 합쳐서 큰 문제를 해결할 수 있어야하고
# 2. 반복되는 문제가 있어야 한다.

N = int(input())
# 각 집이 선택한 색
n = [[0 for _ in range(3)] for _ in range(N)]
arr = []

# R G B
for _ in range(N):
    arr.append(list(map(int, input().split())))

n[0] = arr[0]

for i in range(1, N):
    for j in range(3):
        if j == 0:
            n[i][j] = min(n[i-1][1], n[i-1][2]) + arr[i][j]
        elif j == 1:
            n[i][j] = min(n[i-1][0], n[i-1][2]) + arr[i][j]
        else:
            n[i][j] = min(n[i-1][0], n[i-1][1]) + arr[i][j]

print(min(n[N-1]))