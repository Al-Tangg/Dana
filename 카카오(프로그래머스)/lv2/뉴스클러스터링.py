# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/17677

def solution(str1, str2):
    s1 = []
    s2 = []
    
    # 다중집합 만들기
    for i in range(len(str1) - 1):
        s = str1[i:i+2]
        if s.isalpha():
            s1.append(s.upper())
    for i in range(len(str2) - 1):
        s = str2[i:i+2]
        if s.isalpha():
            s2.append(s.upper())

    gyo = set(s1) & set(s2)
    hap = set(s1) | set(s2)
    
    if len(hap) == 0:
        return 65536
    
    gyo_sum = 0
    hap_sum = 0
    
    # 교집합, 합집합 구하기
    for s in gyo:
        gyo_sum += min(s1.count(s), s2.count(s))
            
    for s in hap:
        hap_sum += max(s1.count(s), s2.count(s))
        
    return int(gyo_sum / hap_sum * 65536)

