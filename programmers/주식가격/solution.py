def solution(prices):
    answer = [0]*len(prices)
    times = []
    
    for idx, price in enumerate(prices):
        while times and prices[times[-1]] > price:
            answer[times[-1]] = idx-times[-1]
            times.pop()
        times.append(idx)
    
    for time in times:
        answer[time] = idx-time    
    
    return answer
