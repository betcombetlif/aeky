# https://programmers.co.kr/learn/courses/30/lessons/81301
# 7분

def solution(s):
    answer = ""
    word_dict = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    import re
    temp = ""
    for i in range(len(s)):
        if re.match("[0-9]", s[i]): # 숫자일 경우
            answer += s[i]
        else:
            temp += s[i]
            if temp in word_dict.keys():
                answer += word_dict[temp]
                temp = ""

    return int(answer)


s = "one4seveneight"
print(solution(s))
