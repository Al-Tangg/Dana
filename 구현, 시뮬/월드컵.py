# https://www.acmicpc.net/problem/6987

answer = []

for _ in range(4):
    result = list(map(int, input().split()))
    ans = '1'
    win = 0
    lose = 0

    for i in range(6):
        if sum(result[i*3: i*3+3]) != 5:
            ans = '0'
            break
        win += result[i*3]
        lose += result[i*3+2]
    
    if win != lose:
        ans = '0'

    for i in range(6):
        for j in range(i+1, 6):
            if result[i*3+1] > 0 and result[j*3+1] > 0:
                result[i*3+1] -= 1
                result[j*3+1] -= 1
        if result[i*3+1] != 0:
            ans = '0'
            break
    
    answer.append(ans)

print(' '.join(answer))
