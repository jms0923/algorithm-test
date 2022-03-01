def solution(citations):
    citations.sort()
    answer = 0
    n = len(citations)
    for idx in range(n):
        h = n-idx
        if citations[idx] >= h:
            return h

    return answer
