def solution(numbers):
    ### 1 - 혼자 풀이
    # 정확성 테스트 4/11 --> 시간 초과
    from collections import defaultdict
    from itertools import permutations
    numbers_str = defaultdict(list)
    for number in numbers:
        numbers_str[str(number)[0]].append(str(number))

    answer = ''
    order = sorted(numbers_str.keys(), reverse=True)
    for key in order:
        temp = [''.join(x) for x in list(permutations(numbers_str[key], len(numbers_str[key])))]
        answer += max(temp)

    return answer

    ### 2 - 참고 풀이
    # https://wooaoe.tistory.com/82
    # numbers = list(map(str, numbers))
    # numbers.sort(key=lambda x: x * 3, reverse=True)
    # return str(int(''.join(numbers)))

    ### 3 - 참고 풀이
    # https://leedakyeong.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B0%80%EC%9E%A5-%ED%81%B0-%EC%88%98-in-python
    # numbers = list(map(str, numbers))
    # answer = ''.join(sorted(numbers, key=lambda x:x (x[0], x[1%len(x)], x[2%len(x)], x[3%len(x)]), reverse=True))
    # return answer if int(answer) != 0 else "0"

param1 = [3, 30, 34, 5, 9]
print(solution(param1))
