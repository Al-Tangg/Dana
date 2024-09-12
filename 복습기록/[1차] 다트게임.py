def solution(dartResult):
    dartResult = dartResult.replace("10", 'K')
    ans = []
    bonus = {'S': 1, 'D': 2, 'T': 3}
    
    i = -1
    
    for d in dartResult:
        if d in bonus:
            ans[-1] = ans[-1] ** bonus[d]
        elif d == '*':
            ans[-1] *= 2
            if i != 0:
                ans[-2] *= 2
        elif d == '#':
            ans[-1] *= (-1)
        else:
            if d == 'K':
                ans.append(10)
            else:
                ans.append(int(d))
            i+=1
    
    return sum(ans)