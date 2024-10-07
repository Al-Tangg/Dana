def solution(today, terms, privacies):
    answer = []
    termMap = dict()
    
    for term in terms:
        t, valid = term.split()
        termMap[t] = int(valid) * 28
    
    t_year, t_month, t_day = list(map(int, today.split('.')))
    
    for i in range(len(privacies)):
        p = privacies[i]
        date, term = p.split()
        year, month, day = list(map(int, date.split('.')))
        
        if (t_year-year) * 12 * 28 + (t_month-month) * 28 + (t_day-day) >= termMap[term]:
            answer.append(i+1)
    
    return answer