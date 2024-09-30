N = int(input())

d = [0] * (N+1)

d[0] = 1
d[1] = 3

for i in range(2, N+1):
    d[i] = (d[i-2] + d[i-1] * 2)%9901

print(d[N])