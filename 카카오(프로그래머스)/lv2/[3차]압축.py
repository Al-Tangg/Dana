# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    answer = []
    words = {chr(j + 64) : j for j in range(1, 27)}
    next_index = 27
    
    i = 0
    while i < len(msg):
        w = msg[i]
        i += 1
        while i < len(msg) and w + msg[i] in words:
            w += msg[i]
            i += 1
        answer.append(words[w])
        
        if i < len(msg):
            words[w + msg[i]] = next_index
            next_index += 1
        
    return answer

# 딕셔너리로 자료형을 수정
# 리스트에서 index()로 찾는 시간: O(n), 딕셔너리 탐색 시간: O(1)