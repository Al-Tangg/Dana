from collections import deque

def solution(queue1, queue2):
    answer = 0
    a = sum(queue1)
    b = sum(queue2)
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    limit = len(queue1) * 4  # 최대 이동 횟수 제한, 제한이 어떻게 되어야하지..
    
    while answer <= limit:
        if a > b:
            val = queue1.popleft()
            queue2.append(val)
            a -= val
            b += val
        elif a < b:
            val = queue2.popleft()
            queue1.append(val)
            a += val
            b -= val
        else:
            return answer
        answer += 1
    
    return -1