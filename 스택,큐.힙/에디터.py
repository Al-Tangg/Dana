# https://www.acmicpc.net/problem/1406

import sys

left = list(sys.stdin.readline().strip())
right = []

N = int(sys.stdin.readline().strip())

for _ in range(N):
    com = sys.stdin.readline().strip()

    if com[0] == 'L' and left:
        right.append(left.pop())
    elif com[0] == 'D' and right:
        left.append(right.pop())
    elif com[0] == 'B' and left:
        left.pop()
    elif com[0] == 'P':
        p, c = com.split()

        left.append(c)
    

print(''.join(left) + ''.join(right[::-1]))
    

    