def solution(tickets):
    answer = ['ICN']
    cant = []

    def dfs(start, tickets):
        if not tickets:
            return
        targets = []
        for idx, ticket in enumerate(tickets):
            if ticket[0] == start:
                targets.append([idx, ticket[1]])
                
        if not targets:
            cant.append(answer.pop())
            dfs(answer[-1], tickets)
        else:
            targets.sort(key= lambda x: x[1])
            now_target = tickets.pop(targets[0][0])
            answer.append(now_target[1])
            dfs(now_target[1], tickets)
    
    dfs('ICN', tickets)
    for can in cant[::-1]:
        answer.append(can)
    return answer
