import sys

answer = sys.maxsize

def dfs(idx, cnt):
    global M, C, answer

    visited[idx] = 1

    if cnt == M - 1:
        ans = 0
        for home in homes:
            h_ans = sys.maxsize
            h_x, h_y = home

            for i in range(C):
                if visited[i] == 1:
                    h_ans = min(h_ans, abs(chicks[i][0] - h_x) + abs(chicks[i][1] - h_y))
        
            ans += h_ans

        answer = min(answer, ans)

    else:
        for i in range(idx + 1, C):
            if visited[i] == 0:
                dfs(i, cnt + 1)
                visited[i] = 0



# 치킨거리 = 집과 가장 가까운 치킨집 사이의 거리
N, M = map(int, sys.stdin.readline().split())
arr = []

# 1은 집 2는 치킨집
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

homes = []
chicks = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            homes.append([i, j])
        elif arr[i][j] == 2:
            chicks.append([i, j])

C = len(chicks)

visited = [0 for _ in range(C)]


for i in range(C):
    dfs(i, 0)
    visited[i] = 0

print(answer)