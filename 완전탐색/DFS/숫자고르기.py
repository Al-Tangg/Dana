import sys

answer = []

def dfs(i, s_num):
    visited[i] = 1

    if visited[arr[i] - 1] == 0:
        dfs(arr[i] - 1, s_num)
    elif s_num == arr[i]:
        answer.append(s_num)


N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

for i in range(N):
    visited = [0 for _ in range(N)]
    dfs(i, i + 1) # idx, 시작 숫자

print(len(answer))

for a in answer:
    print(a)