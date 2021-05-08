# https://programmers.co.kr/learn/courses/30/lessons/42884
# 풀이 참고: https://wwlee94.github.io/category/algorithm/greedy/speed-enforcement-camera/

'''
1. 진출 지점 기준으로 오름 차순 정렬 (routes[1] 기준)
2. 최대 -30000이니 초기 카메라 위치를 -30001로 초기화
3. routes 배열을 반복하면서 카메라가 진입 지점(route[0])보다 작은지 확인
4. 작다면, 현재 카메라 위치로 해당 차량을 만나지 못했다는 의미
    4-1. 카메라를 추가로 세우고
    4-2. 가장 최근 카메라의 위치(route[1])를 갱신
'''


def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])  # routes를 차량이 나간 지점 기준으로 정렬
    camera = -30001  # -30001부터 카메라 위치를 찾는다

    for route in routes:
        if camera < route[0]:
            answer += 1
            camera = route[1]
    return answer


# def solution(routes):
#     from collections import defaultdict
#     time_dict = defaultdict(int)
#     for (in_time, out_time) in routes:
#         for i in range (in_time, out_time+1):
#             time_dict[i] += 1
#
#     answer = []
#     time_list = sorted(time_dict.items(), key=lambda x:x[1], reverse=True) # x[0]: 시점, x[1]: 통행 횟수
#     while sum(val for val in time_dict.values()) > 0:
#         print(">> sum: ", sum(val for val in time_dict.values()))
#         for i in range(len(routes)):
#             if i < len(routes):
#                 print(time_list[0][0], routes[i][0], routes[i][1])
#                 if time_list[0][0] in range(routes[i][0], routes[i][1]+1):
#                     print(">> time: ", time_list[0][0])
#                     if time_list[0][0] not in answer:
#                         answer.append(time_list[0][0])
#                     for j in range(routes[i][0], routes[i][1]+1):
#                         time_dict[j] -= 1
#                     print(time_dict)
#                     routes.remove(routes[i])
#                     time_list = sorted(time_dict.items(), key=lambda x:x[1], reverse=True) # x[0]: 시점, x[1]: 통행 횟수
#
#     return len(answer)


routes = [[-20, 15], [-14, -5], [-18, -13], [-5, -3]]
print(solution(routes))
