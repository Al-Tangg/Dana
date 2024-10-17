import sys
from collections import deque

T = int(sys.stdin.readline())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = []

for _ in range(T):
    w, h = map(int, sys.stdin.readline().split())
    jido = [] # 지도
    ans = 'IMPOSSIBLE'

    for _ in range(h):
        jido.append(list(sys.stdin.readline().strip()))
    
    q1 = deque() # 불 이동
    visited1 = [[0 for _ in range(w)] for _ in range(h)]

    q2 = deque() # 상근이 이동
    visited2 = [[0 for _ in range(w)] for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if jido[i][j] == '@':
                q2.append([i, j])
                visited2[i][j] = 1
            if jido[i][j] == '*':
                q1.append([i, j])
                visited1[i][j] = 1

    t = 0 # 탈출 시간

    while q2:
        f_cnt = len(q1)
        for _ in range(f_cnt):
            x, y = q1.popleft()
                        
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                            
                    # 상근이도 고민
                if 0 <= nx < h and 0 <= ny < w and visited1[nx][ny] == 0 and jido[nx][ny] == '.':
                    q1.append([nx, ny])
                    visited1[nx][ny] = 1
                    jido[nx][ny] = '*'

        cnt = len(q2)
        for _ in range(cnt):
            x, y = q2.popleft()

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                # 상근이가 지도 밖으로 나가면 탈출 성공
                if not (0 <= nx < h and 0 <= ny < w):  # 지도 밖으로 나가는 경우
                    ans = str(t + 1)
                    q2.clear()  # 더 이상 이동할 필요 없으므로 큐를 비우고 탈출
                    break
                
                # 상근이가 이동할 수 있는 경우
                if visited2[nx][ny] == 0 and jido[nx][ny] == '.':
                    q2.append([nx, ny])
                    visited2[nx][ny] = 1
        t += 1
    
    answer.append(ans)

for ans in answer:
    print(ans)