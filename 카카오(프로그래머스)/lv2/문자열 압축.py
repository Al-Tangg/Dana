import sys

def solution(s):
    answer = sys.maxsize
    
    if len(s) == 1:
        return 1
    
    for i in range(1, len(s) // 2 + 1):
        ans = len(s)
        j = 0
        
        while j < len(s):
            k = j
            while s[j:j+i] == s[k:k+i]:
                ans -= i
                k += i
            if k == j + i:
                ans += i
            else:
                ans += (len(str((k - j)//i)) + i)
            j = k
        
        if ans < answer:
            answer = ans
            
    return answer