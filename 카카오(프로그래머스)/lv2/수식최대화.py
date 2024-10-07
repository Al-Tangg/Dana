def calculate(exp, nums):
    if exp == '+':
        return sum(nums)
    elif exp == '-':
        return nums[0] - sum(nums[1:])
    elif exp == '*':
        star = 1
        for num in nums:
            star *= num
        return star
    
def solution(expression):
    answer = 0
    exp = [x for x in ['*', '+', '-'] if x in expression]
    
    if len(exp) == 3:
        for i in range(len(exp)):
            firstPrior = exp[i]
            tmpExp = exp[:]
            tmpExp.remove(firstPrior)
            
            for a in range(2):
                prior = tmpExp[a]
                lower = tmpExp[a-1]

                newExp = expression.split(lower)

                for j in range(len(newExp)):
                    newExp[j] = newExp[j].split(prior)
                    for k in range(len(newExp[j])):
                        newExp[j][k] = calculate(firstPrior, list(map(int, newExp[j][k].split(firstPrior))))
                
                
                for j in range(len(newExp)):
                    newExp[j] = calculate(prior, newExp[j])
                
                result = calculate(lower, newExp)
                
                if answer < abs(result):
                    answer = abs(result)
            
    # 연산자가 2개일 때
    if len(exp) == 2:
        for i in range(2):
            prior = exp[i]
            lower = exp[i-1]
            
            # lower로 split해야 prior로 먼저 계산함
            lowerExp = expression.split(lower)
            for j in range(len(lowerExp)):
                lowerExp[j] = calculate(prior, list(map(int, lowerExp[j].split(prior))))
            
            result = calculate(lower, list(map(int, lowerExp)))
        
            if answer < abs(result):
                answer = abs(result)
    
    if len(exp) == 1:
        answer = abs(calculate(exp[0], list(map(int, expression.split(exp[0])))))
                             
    return answer