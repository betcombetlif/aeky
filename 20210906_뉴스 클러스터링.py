# https://programmers.co.kr/learn/courses/30/lessons/17677

def solution(str1, str2):
    import re
    str1 = ''.join(re.findall('[\w\s]\D+', str1)).upper()
    str2 = ''.join(re.findall('[\w\s]\D+', str2)).upper()
    # print(str1, str2)

    # 다중집합의 원소 만들기
    str1_elem = []
    for i in range(len(str1) - 1):
        if (str1[i] + str1[i + 1]).isalpha():
            str1_elem.append(str1[i] + str1[i + 1])
    # print(str1_elem)

    str2_elem = []
    for i in range(len(str2) - 1):
        if (str2[i] + str2[i + 1]).isalpha():
            str2_elem.append(str2[i] + str2[i + 1])
    # print(str2_elem)

    from collections import Counter
    str1_and_str2 = list((Counter(str1_elem) & Counter(str2_elem)).elements())  # 교집합 구하기
    str1_or_str2 = list((Counter(str1_elem) | Counter(str2_elem)).elements())  # 합집합 구하기
    # print(str1_and_str2, str1_or_str2)

    # 자카드 유사도 구하기
    if not str1_and_str2 and not str1_or_str2:
        return 1 * 65536
    return int(str((len(str1_and_str2) / len(str1_or_str2)) * 65536).split(".")[0])


str1 = "E=M*C^2"
str2 = "e=m*c^2"
print(solution(str1, str2))
