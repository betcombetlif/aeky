# https://programmers.co.kr/learn/courses/30/lessons/12899
# 참고: https://velog.io/@juni416/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-124%EB%82%98%EB%9D%BC%EC%9D%98-%EC%88%AB%EC%9E%90
# 참고: https://velog.io/@dramatic/Algorithm-124-%EB%82%98%EB%9D%BC%EC%9D%98-%EC%88%AB%EC%9E%90

def solution(n):
    answer = ''
    while n > 0:
        if n % 3 == 1:
            answer = '1' + answer
        elif n % 3 == 2:
            answer = '2' + answer
        elif n % 3 == 0:
            answer = '4' + answer
        n = n // 3 - (n % 3 == 0)
    return answer


n = 11
print(solution(n))
