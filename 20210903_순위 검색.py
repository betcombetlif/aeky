# https://programmers.co.kr/learn/courses/30/lessons/72412

def solution(info, query):
    applicants = []
    for i in info:
        applicants.append(i.split())

    answer = [0] * len(query)
    for i in range(len(query)):
        temp = query[i].replace("and", "").split()
        score = temp[-1]
        condition = temp[:-1]
        print(i+1, ">>> 조건: ", score, condition)

        for app in applicants:
            print("> 지원자: ", app)
            flag = False
            if int(app[-1]) >= int(score):
                for c in condition:
                    if c != '-':
                        if c not in app:
                            flag = False
                            break
                        else:
                            flag = True
                    else:
                        flag = True
                if flag:
                    print("check")
                    answer[i] += 1

    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))