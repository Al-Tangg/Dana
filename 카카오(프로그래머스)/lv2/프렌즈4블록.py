# https://school.programmers.co.kr/learn/courses/30/lessons/17679

def solution(m, n, board):
    board = list(map(lambda x: list(x), board))
    flag = True

    while flag:
        flag = False
        tmp = [row[:] for row in board]

        # 현재 보드에서 프렌즈 4블록에 해당하는 거 찾기
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1] != '0' and 'A' <= board[i][j] <= 'Z':
                    tmp[i][j], tmp[i+1][j], tmp[i][j+1], tmp[i+1][j+1] = '0', '0', '0', '0'
                    flag = True
        
        # 떨어뜨리기
        for i in range(m-2, -1, -1):
            for j in range(n):
                if tmp[i][j] != '0':
                    k = i + 1
                    while k < m and tmp[k][j] == '0':
                        k += 1
                    tmp[k-1][j], tmp[i][j] = tmp[i][j], tmp[k-1][j]
                    
        board = tmp
    
    return sum(row.count('0') for row in board)