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