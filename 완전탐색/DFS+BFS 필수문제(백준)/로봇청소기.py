# 청소기가 바라보는 방향이 있음;
# 0은 청소 안된 빈 칸 1은 벽
# 0 - 북 1 - 동 2 - 남 서 - 3

from collections import deque 

N, M = map(int, input().split())
r, c, d = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

q = deque()
q.append([r, c])

while q:
    a, b = q.popleft()

    if arr[a][b] == 0:
        arr[a][b] = 2
    
    flag = 0

    for i in range(4):
        if d == 0:
            d = 3
        else:
            d -= 1

        nx = a + dx[d]
        ny = b + dy[d]

        if arr[nx][ny] == 0:
            q.append([nx, ny])
            flag = 1
            break
    
    if flag == 0:
        nx = a - dx[d]
        ny = b - dy[d]

        if arr[nx][ny] != 1:
            q.append([nx, ny])
        else:
            break

print(sum(row.count(2) for row in arr))