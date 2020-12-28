# def solution(number, k):
#     ### 1 - 혼자 풀이
#     # 정확성 테스트 4/12
#     import itertools
#     number_idx = [i for i in range(len(number))]
#     answer = '000000'
#     for combi in list(itertools.combinations(number_idx, len(number) - k)):
#         temp = ''
#         for c in combi:
#             temp += number[c]
#         if answer < temp:
#             answer = temp
#     return answer

def solution(number, k):
    ### 2 - 참고 풀이
    # https://gurumee92.tistory.com/162
    collected = []

    for (i, num) in enumerate(number):
        while collected and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1

        if k == 0:
            collected += number[i:]
            break

        collected.append(num)

    collected = collected[:-k] if k > 0 else collected
    answer = "".join(collected)
    return answer


param1 = "4177252841"
param2 = 4
print(solution(param1, param2))
