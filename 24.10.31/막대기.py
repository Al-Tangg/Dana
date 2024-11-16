import heapq

X = int(input())

arr = [64]
x = 64

while x != X:
    s = heapq.heappop(arr)
    x -= s

    if x + s//2 < X:
        heapq.heappush(arr, s//2)
        x += (s // 2)
    
    heapq.heappush(arr, s//2)
    x += (s // 2)

print(len(arr))