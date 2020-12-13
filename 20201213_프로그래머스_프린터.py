def solution(priorities, location):
    ### 1 - 혼자 풀이
    # 정확성 테스트 4/20
    size = len(priorities)
    flag = True
    priorities_tuple = []

    for i, priority in enumerate(priorities):
        priorities_tuple.append((i, priority))
        if i == location:
            location = (i, priority)

    while flag:
        for j in range(1, size):
            if priorities_tuple[0][1] < priorities_tuple[j][1]:
                flag = True
                priorities_tuple.append(priorities_tuple[0])
                del priorities_tuple[0]
                break
            else:
                flag = False

    return priorities_tuple.index(location) + 1

    ### 2 - 참고 풀이
    # https://mong9data.tistory.com/29
    # result_location = []
    # current_location = [i for i in range(len(priorities))]
    # while len(priorities) != 0:
    #     if priorities[0] == max(priorities):
    #         result_location.append(current_location.pop(0))
    #         priorities.pop(0)
    #     else:
    #         priorities.append(priorities.pop(0))
    #         current_location.append(current_location.pop(0))
    #
    # return result_location.index(location) + 1




param1 = [1, 1, 9, 1, 1, 1]
param2 = 0
print(solution(param1, param2))