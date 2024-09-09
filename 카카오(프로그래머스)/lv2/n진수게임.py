from collections import deque

def solution(n, t, m, p):
    answer = ""
    jinbup = "0"
    over_num = ["A", "B", "C", "D", "E", "F"]
    nn = 1
    
    while len(jinbup) < t*m:
        tmp = nn
        b = ""
        
        while(tmp):
            namuji = tmp % n
            if namuji >= 10:
                b = over_num[namuji-10] + b
            else:
                b = str(tmp%n) + b
            tmp //= n
        
        nn+=1
        jinbup += b
    
    for i in range(t*m):
        if i % m + 1 == p:
            answer += jinbup[i]

    return answer