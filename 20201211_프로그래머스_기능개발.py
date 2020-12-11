def solution(progresses, speeds):
    ### 1 - 혼자 풀이
    # 정확성 테스트 11/11
    import math

    left = []
    for p, s in zip(progresses, speeds):
        left.append(math.ceil((100-p)/s))

    answer = [1, ]
    num = i = 0
    while i < len(left):
        for j in range(i+1, len(left)):
            # print(answer)

            if left[i] >= left[j]:
                answer[num] += 1
                if j >= len(left) - 1:
                    i = len(left)
            else:
                answer.append(1)
                num += 1
                i = j
                if j >= len(left) - 1:
                    i = len(left)
                break

    return answer


param1 = [95, 90, 99, 99, 80, 99]
param2 = [1, 1, 1, 1, 1, 1]
print(solution(param1, param2))