from collections import deque
import sys


row, col = map(int, sys.stdin.readline().split())
arr = []
pic = []

for r in range(row):
    arr.append(list(map(int, sys.stdin.readline().split())))

visited = [[0 for _ in range(col)] for _ in range(row)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for r in range(row):
    for c in range(col):
        if arr[r][c] == 1 and visited[r][c] == 0:
            q = deque()
            q.append([r, c])
            visited[r][c] = 1
            cnt = 1

            while q:
                x, y = q.popleft()

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < row and 0 <= ny < col and arr[nx][ny] == 1 and visited[nx][ny] == 0:
                        q.append([nx, ny])
                        visited[nx][ny] = 1
                        cnt += 1
            
            pic.append(cnt)

print(len(pic))
print(max(pic) if len(pic) > 0 else 0)