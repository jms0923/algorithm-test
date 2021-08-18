def solution(priorities, location):
    answer = 0
    while priorities:
        if priorities[0] == max(priorities):
            priorities.pop(0)
            answer += 1
            if location == 0:
                break    
        else:
            priorities.append(priorities.pop(0))

        location = location-1 if location != 0 else len(priorities)-1
            
    return answer
