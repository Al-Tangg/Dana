import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().split())
visited = [0 for _ in range(F)]
q = deque()
q.append([S, 0])
visited[S-1] = 1

while q:
    now, cnt = q.popleft()

    if now == G:
        print(cnt)
        exit()
    
    if now + U <= F and visited[now + U - 1] == 0:
        q.append([now + U, cnt + 1])
        visited[now + U - 1] = 1
    
    if now - D >= 1 and visited[now - D - 1] == 0:
        q.append([now - D, cnt + 1])
        visited[now - D - 1] = 1

print("use the stairs")
    

# 강호는 S층에
# G층으로 가야함
# 1층 ~ F층