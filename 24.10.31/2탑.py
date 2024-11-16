import sys

N = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))

answer = [0 for _ in range(N)]
top = []
top.append(0)

for i in range(1, N):
    while len(top) > 0 and arr[top[-1]] <= arr[i]:
        top.pop()
    
    if len(top) > 0:
        answer[i] = top[-1] + 1
    
    top.append(i)

answer = list(map(lambda x: str(x), answer))
print(' '.join(answer))

        