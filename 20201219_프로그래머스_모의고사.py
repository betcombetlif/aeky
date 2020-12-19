def solution(answers):
    ### 1 - 혼자 풀이
    # 정확성 테스트 14/14
    size = len(answers)
    supoza1_pattern = [1, 2, 3, 4, 5] * (size//5+1)
    supoza2_pattern = [2, 1, 2, 3, 2, 4, 2, 5] * (size//8+1)
    supoza3_pattern = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (size//10+1)
    correct = [0, 0, 0]

    for i in range(size):
        if supoza1_pattern[i] == answers[i]:
            correct[0] += 1
        if supoza2_pattern[i] == answers[i]:
            correct[1] += 1
        if supoza3_pattern[i] == answers[i]:
            correct[2] += 1

    answer = []
    for i in range(3):
        if correct[i] == max(correct):
            answer.append(i+1)

    return answer


param1 = [1,2,3,4,5]
print(solution(param1))
