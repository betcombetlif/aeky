def solution(n, lost, reserve):
    ### 1 - 혼자 풀이
    # 정확성 테스트 12/12
    students = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        if i in lost:
            students[i] -= 1
        if i in reserve:
            students[i] += 1

    for i in range(1, n + 1):
        if i < n and students[i] == -1:
            if students[i - 1] == 1:
                students[i] += 1
                students[i - 1] -= 1
            elif students[i + 1] == 1:
                students[i] += 1
                students[i + 1] -= 1

    return students.count(1) + students.count(0) - 1

    ### 2 - 참고 풀이
    # https://rain-bow.tistory.com/entry/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%B2%B4%EC%9C%A1%EB%B3%B5
    # set_reserve = set(reserve) - set(lost)
    # set_lost = set(lost) - set(reserve)
    # for i in set_reserve:
    #     if i-1 in set_lost:
    #         set_lost.remove(i-1)
    #     elif i+1 in set_lost:
    #         set_lost.remove(i+1)
    # return n - len(set_lost)


param1 = 3
param2 = [3]
param3 = [1]

print(solution(param1, param2, param3))
