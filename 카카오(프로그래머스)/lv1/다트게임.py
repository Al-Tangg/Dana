def solution(dartResult):
    i = 0
    bonus_d = {'S': 1, 'D':2, 'T':3}
    dartResult = dartResult.replace("10", 'K')
    
    ans = []
    
    i = -1

    for d in dartResult:
        if d in bonus_d:
            ans[-1] = ans[-1] ** bonus_d[d]
        elif d == '*':
            ans[-1] *= 2
            if i != 0:
                ans[-2] *= 2
        elif d == '#':
            ans[-1] *= (-1)
        else:
            ans.append(10) if d == 'K' else ans.append(int(d))
            i += 1
    
    return sum(ans)