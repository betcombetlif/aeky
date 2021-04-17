### 1 - 혼자 풀이
# 정확성 테스트 8/8
def solution(n, costs):
    answer = 0
    costs = sorted(costs, key=lambda x: x[2])
    connected = [[]]

    def is_connected(param):
        for ci in connected:
            if param[0] in ci and param[1] in ci:
                return True
        return False

    def connect(param):
        for i in range(len(connected)):
            print(param[0], param[1], connected[i])
            if param[0] in connected[i]:
                connected[i].append(param[1])
                print("CHECK1", connected)
                for j in range(len(connected)):
                    if connected[i] != connected[j] and param[1] in connected[j]:
                        connected[i] += connected[j]
                        connected.remove(connected[j])
                        break
                return True
            elif param[1] in connected[i]:
                connected[i].append(param[0])
                print("CHECK2", connected)
                for j in range(len(connected)):
                    if connected[i] != connected[j] and param[0] in connected[j]:
                        connected[i] += connected[j]
                        connected.remove(connected[j])
                        break
                return True
        connected.append([param[0], param[1]])
        print("CHECK3", connected)
        return True

    for cost in costs:
        print(is_connected(cost))
        if is_connected(cost) is False:
            connect(cost)
            answer += cost[2]
        print(connected)
    return answer


param1 = 6
param2 = [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]]
print(solution(param1, param2))
