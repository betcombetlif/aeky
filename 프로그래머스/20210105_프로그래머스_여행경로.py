### 1 - 혼자 풀이
# 정확성 테스트 1/4
def solution(tickets):
    route = ["ICN", ]
    number = len(tickets)
    visited = [False for _ in range(number)]

    while False in visited:
        stack = [i for i in range(number) if 'ICN' == tickets[i][0]]
        while stack:
            if False not in visited:
                return route
            current_idx = stack.pop()
            visited[current_idx] = True
            route.append(tickets[current_idx][1])
            # print(stack, current_idx, visited)
            for i in range(number):
                if visited[i] is False and tickets[current_idx][1] == tickets[i][0]:
                    stack.append(i)
    return route


## 2 - 참고 풀이
# https://copy-driven-dev.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-ProgrammersPython-%EC%97%AC%ED%96%89%EA%B2%BD%EB%A1%9C
# def solution(tickets):
#     tickets.sort(reverse=True)
#     routes = dict()
#     for t1, t2 in tickets:
#         if t1 in routes:
#             routes[t1].append(t2)
#         else:
#             routes[t1] = [t2]
#     st = ['ICN']
#     ans = []
#     while st:
#         top = st[-1]
#         if top not in routes or len(routes[top])==0:
#             ans.append(st.pop())
#         else:
#             st.append(routes[top].pop())
#     ans.reverse()
#     return ans


# param1 = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
param1 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
print(solution(param1))
