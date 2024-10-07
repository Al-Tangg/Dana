# 출발 상근이네, 맥주 20개 가지고 시작
# 50미터에 한 병씩 마심
# 편의점 들려서 맥주 살 수 있으나 한 박스에는 무조건 20병
# 편의점, 끝 점, 시작점이 내가 원하는대로 순서대로 있을 거라는 보장이 없음

from collections import deque
T = int(input()) # 테스트 케이스 개수  

for _ in range(T):
    P = int(input())
    s_x, s_y = map(int, input().split())
    pyons = []
    visited = [0 for _ in range(P)]

    for _ in range(P):
        pyons.append(list(map(int, input().split())))

    e_x, e_y = map(int, input().split())

    q = deque()
    q.append([s_x, s_y])

    ans = 'sad'
    while q:
        x, y = q.popleft() # now

        if abs(e_x - x) + abs(e_y - y) <= 1000:
            ans = 'happy'
            break

        for i in range(len(pyons)):
            p  = pyons[i]

            if visited[i] == 0 and abs(p[0] - x) + abs(p[1] - y) <= 1000:
                q.append(p)
                visited[i] = 1
    
    print(ans)