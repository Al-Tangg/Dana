from collections import deque

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
answer = []

q = deque()

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            q.append([i,j])
            visited[i][j] = 1
            ans = 0

            while q:
                x, y = q.popleft()
                ans += 1

                dx = [1, -1, 0, 0]
                dy = [0, 0, 1, -1]

                    
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1 and visited[nx][ny] == 0:
                        q.append([nx, ny])
                        visited[nx][ny] = 1

            answer.append(ans)

answer.sort()
print(len(answer))
for a in answer:
    print(a)


