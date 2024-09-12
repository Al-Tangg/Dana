def solution(n, t, m, p):
    answer = []
    jinsu = "0"
    num = 1
    alpha = ["A", "B", "C", "D", "E", "F"]
    
    while len(jinsu) < t*m:
        jin = ""
        tmp_num = num
        
        while tmp_num:
            namuji = tmp_num % n
            if namuji >= 10:
                jin = alpha[namuji-10] + jin
            else:
                jin = str(tmp_num%n) + jin
            tmp_num //= n
            
        num += 1
        jinsu += jin
    
    i = 0
    while len(answer) < t:
        if i % m + 1 == p:
            answer.append(jinsu[i])
        i += 1
    
    return ''.join(answer)