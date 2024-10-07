from collections import deque

def solution(bridge_length, weight, truck_weights):
    q = deque([0 for _ in range(bridge_length-1)])
    
    t = 1
    i = 1
    sum = truck_weights[0]
    
    q.append(truck_weights[0])
    
    while sum > 0:
        sum -= q.popleft()
        
        
        if i < len(truck_weights) and sum + truck_weights[i] <= weight:
            q.append(truck_weights[i])
            i += 1
            sum += truck_weights[i]
        else:
            q.append(0)
        
        t += 1
            
    return t