def solution(numbers):
    numbers = [str(num) for num in numbers]
    numbers.sort(key= lambda num: num*3, reverse=True)
    answer = str(int(''.join(numbers))) # remove zero
    
    return answer
