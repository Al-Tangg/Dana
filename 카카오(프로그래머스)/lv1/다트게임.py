def solution(dartResult):
    i = 0
    bonus_d = {'S': 1, 'D':2, 'T':3}
    ans = []
    
    while i < len(dartResult):
        tmp_s = ""
        while dartResult[i].isdigit():
            tmp_s += dartResult[i]
            i+=1
            
        score = int(tmp_s)
        bonus = dartResult[i]
        i+=1 
        
        ans.append(score ** bonus_d[bonus])
        
        # 아차상
        if i < len(dartResult) and not dartResult[i].isdigit():
            if dartResult[i] == '#':
                ans[-1] *= (-1)
            elif dartResult[i] == '*':
                if i != 2:
                    ans[-2] *= 2
                ans[-1] *= 2
            i += 1
    
    return sum(ans)