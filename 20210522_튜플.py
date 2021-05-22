# https://programmers.co.kr/learn/courses/30/lessons/64065

'''
1. s 양끝의 {}를 삭제한다
2. {}를 기준으로 element를 추출한 리스트(s_list)를 만든다
3. s_list를 for문으로 돌면서 element 별 등장 횟수를 센다
4. 등장 횟수로 정렬하여 answer를 도출한다
'''


def solution(s):
    s = s[1:-1]  # 1
    s_list = []

    i = 0
    while i < len(s):
        if s[i] == "{":
            tmp_num = ""
            for j in range(i + 1, len(s)):
                if s[j] == "}":
                    i = j
                    s_list.append(tmp_num.split(",")) # 2
                    break
                else:
                    tmp_num += s[j]
        i += 1

    from collections import defaultdict
    s_dict = defaultdict(int)
    for elem in s_list:
        for e in elem:
            s_dict[e] += 1 # 3

    answer = []
    for (key, value) in sorted(s_dict.items(), key=lambda x: x[1], reverse=True): # 4
        answer.append(int(key))

    return answer


s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(s))
