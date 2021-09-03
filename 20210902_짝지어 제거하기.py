# https://programmers.co.kr/learn/courses/30/lessons/12973
# 참고: https://velog.io/@rapsby/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A7%9D%EC%A7%80%EC%96%B4-%EC%A0%9C%EA%B1%B0%ED%95%98%EA%B8%B0-python

def solution(s):
    stack = [s[0]]

    for c in s[1:]:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    if stack:
        return 0
    return 1



s = "aazaaasasss"
print(solution(s))