# 출발 상근이네, 맥주 20개 가지고 시작
# 50미터에 한 병씩 마심
# 편의점 들려서 맥주 살 수 있으나 한 박스에는 무조건 20병
# 편의점, 끝 점, 시작점이 내가 원하는대로 순서대로 있을 거라는 보장이 없음

T = int(input())

for t in range(T):
    P = int(input())
    pyons = []
    ans = 'happy'

    s_x, s_y = map(int, input().split())
    for p in range(P):
        pyons.append(list(map(int, input().split())))
    
    e_x, e_y = map(int, input().split())

    pyons.sort(key = lambda x : (x[0] - s_x + x[1] -s_y))
    
    for pyon in pyons:
        p_x, p_y = pyon

        if p_x - s_x + p_y - s_y <= 1000:
            s_x, s_y = p_x, p_y
        else:
            ans = 'sad'
            break
    
    if e_x - s_x + e_y - s_y > 1000:
        ans = 'sad'

    print(ans)