# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    answer = []
    words = [chr(65+c) for c in range(26)]
    
    i = 0
    while i < len(msg):
        w = msg[i]
        i += 1
        while i < len(msg) and w + msg[i] in words:
            w += msg[i]
            i += 1
        answer.append(words.index(w) + 1)
        
        if i < len(msg):
            words.append(w + msg[i])
        
    return answer