# 출발 상근이네, 맥주 20개 가지고 시작
# 50미터에 한 병씩 마심 -> 한 번 맥주 리필하면 1000m 갈 수 있음
# 편의점 들려서 맥주 살 수 있으나 한 박스에는 무조건 20병
# 편의점, 끝 점, 시작점이 내가 원하는대로 순서대로 있을 거라는 보장이 없음

from collections import deque
T = int(input()) # 테스트 케이스 개수  

for _ in range(T):
    n = int(input()) # 편의점 개수
    s_x, s_y = map(int, input().split()) # 상근이 집

    pyons = [] # 편의점 위치들
    for _ in range(n):
        pyons.append(list(map(int, input().split())))

    e_x, e_y = map(int, input().split()) # 락 페스티벌 좌표

    ans = 'sad'

    q = deque()
    visited = [0 for _ in range(n)] # 편의점 방문 유무
    q.append([s_x, s_y])

    while q:
        x, y = q.popleft()

        if abs(x - e_x) + abs(y - e_y) <= 1000:
            ans = 'happy'
            break

        for i in range(n):
            p_x, p_y = pyons[i]
            if abs(x - p_x) + abs(y - p_y) <= 1000 and visited[i] == 0:
                q.append([p_x, p_y])
                visited[i] = 1
                
    print(ans)