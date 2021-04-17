def solution(bridge_length, weight, truck_weights):
    ### 1 - 혼자 풀이
    # 정확성 테스트 14/14
    truck_num = len(truck_weights)
    time = 0
    out_bridge = 0
    on_bridge = []
    i = 0

    while out_bridge < truck_num and i < truck_num:
        for truck in on_bridge:
            if truck[0] == time - bridge_length:
                on_bridge.remove(truck)
                out_bridge += 1
                break
        if sum(truck for arrived_time, truck in on_bridge) + truck_weights[i] <= weight:
            on_bridge.append((time, truck_weights[i]))
            i += 1

        time += 1
        # print(time, on_bridge)

    time += bridge_length

    return time


param1 = 100
param2 = 100
param3 = [10]
print(solution(param1, param2, param3))
