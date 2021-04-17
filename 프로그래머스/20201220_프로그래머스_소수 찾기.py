### 1 - 혼자 풀이
# 정확성 테스트 12/12
def is_prime(number):
    if number < 2:
        return False
    m = int(number ** 0.5)
    for i in range(2, m + 1):
        if number % i == 0:
            return False
    return True

def solution(numbers):
    from itertools import permutations
    numbers_list = [number for number in numbers]
    permut_list = []
    for i in range(1, len(numbers)+1):
        temp = list(permutations(numbers_list, i))
        for j in range(len(temp)):
            temp[j] = int(''.join(temp[j]))
        permut_list += temp

    answer = 0
    for permut in set(permut_list):
        if is_prime(permut) == True:
            answer += 1
    return answer


param1 = "011"
print(solution(param1))