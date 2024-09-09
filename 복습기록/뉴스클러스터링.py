def solution(str1, str2):
    l1 = []
    l2 = []
    
    for i in range(len(str1) - 1):
        w = str1[i:i+2].upper()
        if w.isalpha():
            l1.append(w)
        
    for i in range(len(str2) - 1):
        w = str2[i:i+2].upper()
        if w.isalpha():
            l2.append(w)
    
    if len(l1) == 0 and len(l2) == 0:
        return 65536
    
    s1 = set(l1)
    s2 = set(l2)
    
    gyo = s1 & s2
    hap = s1 | s2
    
    gyo_sum = 0
    hap_sum = 0
    
    for a in gyo:
        gyo_sum += min(l1.count(a), l2.count(a))
    
    for a in hap:
        hap_sum += max(l1.count(a), l2.count(a))
    
    return int(gyo_sum/hap_sum*65536)