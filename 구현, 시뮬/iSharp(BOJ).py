# https://www.acmicpc.net/problem/3568
import sys

s = sys.stdin.readline()
s = s.replace(',', '').replace(';', '')
s = s.split()

type = ['&', '[', ']', '*'] # 변수형(기본 변수형 제외)

for i in range(1, len(s)):
    new_t = ''
    for j in range(len(s[i])-1, -1, -1):
        if s[i][j] in type:
            new_t += s[i][j]
        else:
            break
    
    new_t = new_t.replace('][', '[]')
    new_s = s[0] + new_t + ' ' + s[i][:j+1] + ';'

    print(new_s)
    


# 기본변수형[변수형] 변수선언(,''를 그거로)