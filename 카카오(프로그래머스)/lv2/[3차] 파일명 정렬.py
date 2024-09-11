def solution(files):
    arr = []
    
    for f in files:
        i = 0
        head = []
        number = []
        
        while not f[i].isdigit():
            head.append(f[i])
            i += 1
        while i < len(f) and f[i].isdigit():
            number.append(f[i])
            i += 1
        
        arr.append([f, ''.join(head).upper(), ''.join(number)])
    
    arr.sort(key = lambda x: (x[1], int(x[2])))
    
    return [x[0] for x in arr]

# 영문대소문자, 숫자, 공백, (, ), ., - 로 이루어짐
# 영문자로 시작, 숫자를 하나 이상 포함
# HEAD - NUMBER - TAIL