def balance(w, s):
    if len(w) == 0:
        return ''
    
    # 2번: u, v 분할하기
    l = 0
    r = 0
    
    for j in range(len(w)):
        gal = w[j]
        if gal == '(':
            l += 1
        else:
            r += 1
        if l == r:
            break
    
    u = w[:j+1]
    v = w[j+1:]
    
    # 3번: u가 올바른 괄호 문자열인지 확인
    for i in u:
        if i == '(':
            s.append('(')
        elif s and i == ')':
            s.pop()
    
    # 3-1번
    if len(s) == 0:
        return u + balance(v, s)
    # 4번
    else:
        # 4-4: u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
        new_u = []
        for i in u[1:-1]:
            if i == '(':
                new_u.append(')')
            else:
                new_u.append('(')
        s.clear()
        return '(' + balance(v, s) + ')' + ''.join(new_u)

def solution(p):
    answer = ''
    s = []
    answer = balance(p, s)
    
    return answer