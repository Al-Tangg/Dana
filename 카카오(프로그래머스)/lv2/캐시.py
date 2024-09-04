# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/17680

from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque(maxlen = cacheSize)
    
    for c in cities:
        upperC = c.upper()
        if upperC in cache:
            answer += 1
            cache.remove(upperC)
            cache.append(upperC)
        else:
            answer += 5
            cache.append(upperC)

    return answer