# https://programmers.co.kr/learn/courses/30/lessons/72411

def solution(orders, course):
    answer = []

    from itertools import combinations

    substr_list = []
    for order in orders:
        for number in course:
            substr_list += combinations(order, number)

    for i in range(len(substr_list)):
        substr_list[i] = tuple(sorted(substr_list[i]))
    substr_list = set(substr_list)
    print(substr_list)

    from collections import defaultdict

    course_dict = defaultdict(lambda: 0)
    for order in orders:
        for substr in substr_list:
            flag = True
            for letter in substr:
                if letter not in order:
                    flag = False
                    break
            if flag is True:
                course_dict[''.join(substr)] += 1
    print(course_dict)

    len_course_dict = defaultdict(list)
    for (key, value) in course_dict.items():
        len_course_dict[len(key)].append((key, value))
    print(len_course_dict)

    for key in len_course_dict.keys():
        if key in course:
            tmp = sorted(len_course_dict[key], key=lambda x: x[1], reverse=True)
            last = 0
            for t in tmp:
                if course_dict[t[0]] >= 2 and t[1] >= last:
                    answer.append(t[0])
                    last = t[1]

    return sorted(answer)


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]
print(solution(orders, course))
