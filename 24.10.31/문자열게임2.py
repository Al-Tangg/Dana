import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    alpha = [[] for _ in range(26)]

    W = sys.stdin.readline().strip()
    K = int(sys.stdin.readline().strip())

    for i in range(len(W)):
        w = W[i]

        alpha[ord(w) - 97].append(i)
    
    s = sys.maxsize
    l = -1

    for a in alpha:
        if len(a) >= K:
            for i in range(len(a) - K + 1):
                s = min(s, a[i+K-1] - a[i] + 1)
                l = max(l, a[i+K-1] - a[i] + 1)
    
    if l == -1:
        print(-1)
    else:
        print(s, l)



# 문자열의 첫번째 