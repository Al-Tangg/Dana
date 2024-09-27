N = int(input())
arr = list(map(int, input().split()))
dec_arr = arr[::-1]

inc = [1] * N # 증가 중
dec = [1] * N # 감소 중


for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            inc[i] = max(inc[i], inc[j] + 1)
        if dec_arr[i] > dec_arr[j]:
            dec[i] = max(dec[i], dec[j] + 1)
            
result = 0
for i in range(N):
    if inc[i] + dec[N-i-1] - 1 > result:
        result = inc[i] + dec[N-i-1] - 1
    
print(result)