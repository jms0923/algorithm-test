import math
from itertools import permutations


def is_prime(num):
    if num == 0 or num == 1: return False
    for i in range(2, int(math.sqrt(num))+1):
        if num%i==0: return False
    return True

def solution(numbers):
    answer = []
    if is_prime(int(numbers)): answer.append(int(numbers))
    
    for now_len in range(1, len(numbers)+1):
        now_per = list(permutations(numbers, now_len))
        for now_set in now_per:
            now_num = int(''.join(now_set))
            if is_prime(now_num):
                answer.append(now_num)
    
    return len(set(answer))
