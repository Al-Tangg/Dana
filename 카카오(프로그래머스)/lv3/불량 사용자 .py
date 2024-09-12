def dfs(i, visited, banned_user, ans, answer):
        if i == len(banned_user):
            answer.add(tuple(sorted(ans)))
            return
        
        for s in banned_user[i]:
            if visited[s] == False:
                visited[s] = True
                dfs(i+1, visited, banned_user, ans + (s,), answer)
                visited[s] = False
            
def solution(user_id, banned_id):
    answer = set()
    banned_user = []
    visited = {x: False for x in user_id}
    
    for b in banned_id:
        b_l = len(b)
        b_u = []
        for u in user_id:
            flag = False
            if len(u) == b_l:
                for bb, uu in zip(b, u):
                    if bb!=uu and bb!='*':
                        flag = True
                        break
            else:
                flag = True
            if flag == False:
                b_u.append(u)
        banned_user.append(b_u)

    dfs(0, visited, banned_user, (), answer)

    return len(answer)



# product를 사용한 예시
from itertools import product

def solution(user_id, banned_id):
    answer = set()
    banned_user = []
    
    # 각 banned_id 마다 불량 사용자가 될 수 있는 user_id 담기
    for b in banned_id:
        b_l = len(b)
        b_u = []
        for u in user_id:
            flag = False
            if len(u) == b_l:
                for bb, uu in zip(b, u):
                    if bb!=uu and bb!='*':
                        flag = True
                        break
            else:
                flag = True
            if flag == False:
                b_u.append(u)
        banned_user.append(b_u)
    
    pro_banned_user = list(product(*banned_user))
    
    for pro in pro_banned_user:
        if len(pro) == len(set(pro)):
            answer.add(tuple(sorted(pro)))

    return len(answer)