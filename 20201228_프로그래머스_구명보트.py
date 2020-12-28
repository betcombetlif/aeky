def solution(people, limit):
    ### 1 - 혼자 풀이
    # 정확성 테스트 15/15, 효율성 테스트 0/5
    answer = 0
    people.sort(reverse=True)
    while len(people) > 0:
        left = limit - people[0]
        people.pop(0)
        answer += 1
        for j in range(0, len(people)):
            if left >= people[j]:
                people.pop(j)
                break
        print(left, people, answer)
    return answer

### 2 - 참고 풀이
# https://leedakyeong.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B5%AC%EB%AA%85%EB%B3%B4%ED%8A%B8-in-python
# def solution(people, limit):
#     people.sort()
#     answer = 0
#     i = 0
#     j = len(people) - 1
#     while i <= j:
#         answer += 1
#         if people[i] + people[j] <= limit:
#             i += 1
#         j -= 1
#     return answer


param1 = [20, 30, 40, 30]
param2 = 60
print(solution(param1, param2))
