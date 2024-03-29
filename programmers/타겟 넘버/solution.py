def dfs(array, numbers, target, size):
    answer = 0
    
    if len(array) == size:
        if sum(array) == target:
            return 1
        else:
            return 0
    else:
        tmpNum = numbers.pop(0)
        array.append(tmpNum)
        answer += dfs(array, numbers, target, size)
        array.pop()
        array.append(-tmpNum)
        answer += dfs(array, numbers, target, size)
        array.pop()
        numbers.append(tmpNum)
        
        return answer
    

def solution(numbers, target):
    answer = 0

    answer += dfs([numbers[0]], numbers[1:], target, len(numbers))
    answer += dfs([-numbers[0]], numbers[1:], target, len(numbers))
    
    return answer
