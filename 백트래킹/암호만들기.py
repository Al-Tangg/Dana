# https://www.acmicpc.net/problem/1759

import sys

result = []
jaem = ['a', 'e', 'i', 'o', 'u']

def dfs(idx, word, ja, mo):
    global L, C

    visited[idx] = 1

    if len(word) == L and ja >= 1 and mo >= 2:
        result.append(word)
    
    else:
        for i in range(idx + 1, C):
            if arr[i] in jaem:
                dfs(i, word + arr[i], ja + 1, mo)
            else:
                dfs(i, word + arr[i], ja, mo + 1)
            
            visited[i] = 0

L, C = map(int, sys.stdin.readline().split())
arr = list(sys.stdin.readline().split())

arr.sort()

for i in range(C - L + 1):
    visited = [0 for _ in range(C)]
    
    if arr[i] in jaem:
        dfs(i, arr[i], 1, 0)
    else:
        dfs(i, arr[i], 0, 1)

for r in result:
    print(r)
# 암호 서로 다른 L개의 알파벳 소문자로 구성
# 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성
# 오름차순일 가능성 높음