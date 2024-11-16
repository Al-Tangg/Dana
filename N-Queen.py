# https://www.acmicpc.net/problem/9663

from itertools import combinations

N = int(input())

answer = 0

for combi in combinations(range(N*N), N):
    flag = True
    
    for i in range(N):
        x1, y1 = combi[i] // N, combi[i] % N
        for j in range(i + 1, N):
            x2, y2 = combi[j] // N, combi[j] % N

            if x1 == x2 or y1 == y2 or abs(x1-x2) == abs(y1-y2):
                flag = False
                break
        
            if flag:
                answer += 1

print(answer)
