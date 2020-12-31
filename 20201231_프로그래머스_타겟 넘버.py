### 1 - 혼자 풀이
# 시간 초과
# def solution(numbers, target):
#     size = len(numbers)
#     for i in range(size):
#         numbers.append(-numbers[i])
#
#     import itertools
#     answer = 0
#     possibilities = set(itertools.permutations(numbers, size))
#     for possibility in possibilities:
#         if sum(possibility) == target:
#             answer += 1
#     return answer

### 2 - 참고 풀이
# https://eda-ai-lab.tistory.com/475
def solution(numbers, target):
    from itertools import product
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)


param1 = [1, 1, 1, 1, 1]
param2 = 3
print(solution(param1, param2))
