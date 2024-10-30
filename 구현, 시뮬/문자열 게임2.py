# https://www.acmicpc.net/problem/20437

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    W = sys.stdin.readline().strip()
    K = int(sys.stdin.readline())

    alphas = [[] for _ in range(27)]

    for i in range(len(W)):
        w = W[i]

        alphas[ord(w) - 97].append(i)
    
    min_l = sys.maxsize
    max_l = 0

    for a in alphas:
        if len(a) >= K:
            i = 0
            while i + K - 1 < len(a):
                l = a[i+K-1] - a[i] + 1

                if l < min_l:
                    min_l = l
                if l > max_l:
                    max_l = l
                
                i += 1

    if min_l == sys.maxsize and max_l == 0:
        print(-1)
    else:
        print(min_l, max_l)




# 결국에 3번은 양 끝이 어떤 문자이면서 어떤 문자를 K개 포함하는 경우고
# 4번은 양 끝이 어떤 문자이면서 어떤 문자를 K개 포함하는 경우네
# 일단 어떤 문자가 문자열 안에 K개 이상 있어야 함