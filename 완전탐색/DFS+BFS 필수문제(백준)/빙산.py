import sys
from collections import deque

def bfs(x, y):
     q = deque()
     q.append([x, y])
     visited[x][y] = 1

     while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                if bingsan[nx][ny] > 0:
                    q.append([nx, ny])
                    visited[nx][ny] = 1
                elif bingsan[x][y] > 0:
                    bingsan[x][y] -= 1
    
     return 1


N, M = map(int, sys.stdin.readline().split())
bingsan = []
answer = 0

for _ in range(N):
    bingsan.append(list(map(int, sys.stdin.readline().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while True:
     visited = [[0 for _ in range(M)] for _ in range(N)]
     cnt = 0

     for i in range(N):
          for j in range(M):
               if bingsan[i][j] > 0 and visited[i][j] == 0:
                    cnt += bfs(i, j)

     if cnt > 1:
        print(answer)
        exit()

     if cnt == 0:
          print(0)
          exit()
    
     answer += 1

                                        
                                         
                                         

