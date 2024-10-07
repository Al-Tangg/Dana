import heapq

def solution(operations):
    answer = []
    
    minHeap = []
    maxHeap = []
    
    for op in operations:
        command, num = op.split()
        
        if command == 'I':
            heapq.heappush(minHeap, int(num))
            heapq.heappush(maxHeap, -int(num))
        else:
            if num == '-1' and minHeap:
                value = heapq.heappop(minHeap)
                maxHeap.remove(-value)
            elif num == '1' and maxHeap:
                value = heapq.heappop(maxHeap)
                minHeap.remove(-value)
    
    return [-heapq.heappop(maxHeap), heapq.heappop(minHeap)] if len(minHeap) > 0 else [0,0]