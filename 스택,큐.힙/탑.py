import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

ans = ['0' for _ in range(N)]
stack = []

stack.append(0)

for i in range(1, N):
    if arr[stack[-1]] > arr[i]:
        stack.pop()
    
    if len(stack) > 0:
        ans[i] = str(stack[-1] + 1)

    stack.append(i)

if all(x == '0' for x in ans):
    print(0)
else:
    print(' '.join(ans)) 
