from collections import deque


def check_one_diff(target_1, target_2):
    dist = 0
    for t1, t2 in zip(target_1, target_2):
        if t1 != t2:
            dist+=1
        if dist > 1: return False
            
    return True

def solution(begin, target, words):
    if target not in words:
        return 0
    depths = []
    def dfs(now_target, words, depth):
        if now_target == target:
            depths.append(depth)
        for idx, word in enumerate(words):
            if check_one_diff(word, now_target):
                dfs(word, words[:idx]+words[idx+1:], depth+1)
                
    dfs(begin, words, 0)
        
    return min(depths)
