from collections import deque


def solution(n, computers):
    answer = 0
    visit = [False]*n
    for i in range(n):
        computers[i][i] = 0
    queue = deque()
    queue.append(0)

    while False in visit:
        if not queue:
            answer+=1
            queue.append(visit.index(False))
            continue
            
        node = queue.pop()
        if not visit[node]:
            visit[node] = True
            will_visit = [i for i, n in enumerate(computers[node]) if n==1]
            queue.extend(will_visit)
    
    return answer+1
