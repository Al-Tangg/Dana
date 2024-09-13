from itertools import product

def solution(user_id, banned_id):
    answer = []
    banned_users = []
    
    # 불량 사용자 id일 수 있는 사용자들 각각 구하기
    for ban in banned_id:
        banned = []
        for user in user_id:
            if len(ban) == len(user):
                flag = True
                for u, b in zip(user, ban):
                    if u != b and b != '*':
                        flag = False
                        break
                if flag:
                    banned.append(user)
        banned_users.append(banned)
    
    pro = list(product(*banned_users))
    
    for p in pro:
        if len(set(p)) == len(p):
            answer.append(tuple(sorted(p)))
    
    return len(set(answer))