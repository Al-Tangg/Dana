def solution(gems):
    answer = []
    bosuks = set(gems)
    tmp_bosuks = {}
    s = 0
    e = 0
    
    while e < len(gems):   
        if gems[e] in tmp_bosuks:
            tmp_bosuks[gems[e]] += 1
        else:
            tmp_bosuks[gems[e]] = 1
        
        while len(tmp_bosuks) == len(bosuks):
            answer.append([s+1, e+1])
            if tmp_bosuks[gems[s]] > 1:
                tmp_bosuks[gems[s]] -=1
            else:
                del tmp_bosuks[gems[s]]
            s += 1
        e += 1
    
    result = answer[0]
    
    for a in answer:
        if a[1] - a[0] < result[1] - result[0]:
            result = a
    return result

# 진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아 구매