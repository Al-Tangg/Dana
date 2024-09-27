n = int(input())

d = [[0 for _ in range(n)] for _ in range(n)]
nums = []

for _ in range(n):
    nums.append(list(map(int, input().split())))

d[0][0] = nums[0][0]

for i in range(1, n):
    for j in range(len(nums[i])):
        if j == 0:
            d[i][j] = d[i-1][j] + nums[i][j]
        elif j == len(nums[i]):
            d[i][j] = d[i-1][j-1] + nums[i][j]
        else:
            d[i][j] = max(d[i-1][j-1], d[i-1][j]) + nums[i][j]

print(max(d[n-1]))