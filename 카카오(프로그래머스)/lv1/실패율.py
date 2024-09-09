# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    answer = {}

    a = len(stages)

    for i in range(1, N+1):
        if i in stages:
            cnt = stages.count(i)
            answer[i] = cnt / a
            a -= cnt
        else:
            answer[i] = 0
    
    return sorted(answer, key = lambda x: -answer[x])