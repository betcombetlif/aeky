# https://programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    answer = ''
    for i in range(len(s)):
        if s[i] == ' ':
            answer += s[i]
        elif i == 0 or (i > 0 and s[i-1] == ' '):
            answer += s[i].upper()
        else:
            answer += s[i].lower()
    return answer


s = " adgagd 3eagdag "
print(solution(s))