import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

answer = 0

for i in range(N):
    num = arr[i]

    l = 0
    r = N - 1

    while l < r:
        value = arr[l] + arr[r]

        if value == num:
            if l == i:
                l += 1
            elif r == i:
                r -= 1
            else:
                answer += 1
                break
        elif value > num:
            r -= 1
        else:
            l += 1

print(answer)