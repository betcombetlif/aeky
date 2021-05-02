# https://programmers.co.kr/learn/courses/30/lessons/68646

def solution(balloons):
    answer = 0
    left = 0

    while left < len(balloons):
        tmp = balloons[:]
        left_num = balloons[left]
        print("LEFT_NUM: ", left_num)

        cond = True  # 사용 시 False로 바뀜
        curr = 0

        while len(tmp) > 0:
            if len(tmp) == 1 and left_num == tmp[0]:
                answer += 1
                print("CHECK!", left_num, answer)
                break

            print(">> ", tmp, curr)
            if curr + 1 < len(tmp):
                if tmp[curr] == left_num:
                    if tmp[curr] > tmp[curr + 1]:
                        if cond is True:
                            cond = False
                            tmp.pop(curr + 1)
                            curr = curr + 1
                        else:
                            break
                    else:
                        tmp.pop(curr + 1)
                elif tmp[curr + 1] == left_num:
                    if tmp[curr] < tmp[curr + 1]:
                        if cond is True:
                            cond = False
                            tmp.pop(curr)
                            curr = curr + 1
                        else:
                            break
                    else:
                        tmp.pop(curr)
                else:
                    if tmp[curr] > tmp[curr + 1]:
                        tmp.pop(curr)
                    else:
                        tmp.pop(curr + 1)
            else:
                print("COND: ", cond)
                if cond is True:
                    if tmp[0] == left_num:
                        tmp.pop(1)
                    elif tmp[1] == left_num:
                        tmp.pop(0)
                else:
                    if tmp[0] == left_num:
                        if tmp[0] < tmp[1]:
                            tmp.pop(1)
                        else:
                            break
                    elif tmp[1] == left_num:
                        if tmp[0] > tmp[1]:
                            tmp.pop(0)
                        else:
                            break

        left += 1

    return answer


a = [9, -1, -5]
print(solution(a))


# 참고 풀이
# https://velog.io/@eehwan/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%92%8D%EC%84%A0-%ED%84%B0%ED%8A%B8%EB%A6%AC%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC
#
# def solution(a):
#     result = [False for _ in range(a)]
#     minFront, minRear = float("inf"), float("inf")
#     for i in range(len(a)):
#         if a[i] < minFront:
#             minFront = a[i]
#             result[i] = True
#         if a[-1-i] < minRear:
#             minRear = a[-1-i]
#             result[-1-i] = True
#     return sum(result)
