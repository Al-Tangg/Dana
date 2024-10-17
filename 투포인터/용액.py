import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

l = 0
r = N - 1

s = (arr[0], arr[N-1])

while l < r:
    value = arr[l] + arr[r]

    if abs(value) < abs(sum(s)):
        s = arr[l], arr[r]

    if value == 0:
        print(arr[l], arr[r])
        exit()
    elif value < 0:
        l += 1
    else:
        r -= 1

print(s[0], s[1])