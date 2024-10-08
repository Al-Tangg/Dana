from queue import PriorityQueue

def solution(jobs):
    answer = []
    
    q = PriorityQueue()
    jobs.sort(key = lambda x: x[0])
        
    t = jobs[0][0] # 현재 시각
    i = 0
    
    while not q.empty() or i < len(jobs):
        for j in range(i, len(jobs)):
            job = jobs[j]
            if job[0] <= t:
                q.put((job[1], job))
                i += 1
        
        if not q.empty():
            p = q.get()[1]
            answer.append(t - p[0] + p[1])
            t += p[1]
        else:
            t += 1
            
    return sum(answer) // len(answer)