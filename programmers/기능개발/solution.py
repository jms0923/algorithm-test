import numpy as np

def solution(progresses, speeds):
    answer = []
    
    rest = np.full((1, len(progresses)), 100)
    progresses = np.array(progresses)
    speeds = np.array(speeds)
    
    rest = np.ceil((rest-progresses)/speeds).astype(np.int64).tolist()[0]

    before_rest_day = 0
    for now_rest_day in range(1, len(rest)):
        if rest[before_rest_day] < rest[now_rest_day]:
            deploy_task = answer[-1] if answer else 0
            answer.append(now_rest_day-before_rest_day)
            before_rest_day = now_rest_day
    
    answer.append(len(rest)-before_rest_day)
        
    return answer
