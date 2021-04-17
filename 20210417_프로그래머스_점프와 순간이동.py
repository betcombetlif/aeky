# https://programmers.co.kr/learn/courses/30/lessons/12980
# 통과

def solution(n):
    ans = 0

    while n / 2 > 0:
        if n % 2 == 1:
            ans += 1
            n -= 1
        else:
            n = n / 2

    return ans


n = 5
print(solution(n))