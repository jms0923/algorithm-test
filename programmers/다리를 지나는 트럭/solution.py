from queue import Queue


def solution(bridge_length, weight, truck_weights):
    driving_trucks = Queue(bridge_length)
    driving_times = []
    now_weight = 0
    answer = 0

    while truck_weights or not driving_trucks.empty():
        if driving_times:
            driving_times = list(map(lambda x: x+1, driving_times))
            if driving_times[0] > bridge_length:
                now_weight -= driving_trucks.get()
                driving_times.pop(0)
        if truck_weights and weight >= now_weight + truck_weights[0]:
            now_weight += truck_weights[0]
            driving_trucks.put(truck_weights.pop(0))
            driving_times.append(1)
                
        answer += 1
    
    return answer
