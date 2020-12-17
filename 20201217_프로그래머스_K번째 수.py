def solution(array, commands):
    ### 1 - 혼자 풀이
    # 정확성 테스트 7/7
    answer = []
    for command in commands:
        answer.append(sorted(array[command[0]-1:command[1]])[command[2]-1])
    return answer


param1 = [1, 5, 2, 6, 3, 7, 4]
param2 = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(param1, param2))
