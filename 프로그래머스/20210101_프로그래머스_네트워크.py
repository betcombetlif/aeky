### 1 - 혼자 풀이
# 정확성 테스트 13/13
def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    stack = []
    while False in visited:
        stack.append(visited.index(False))
        while stack:
            current = stack.pop()
            visited[current] = True
            for i in range(n):
                if computers[current][i] == 1 and visited[i] is False:
                    stack.append(i)
        answer += 1
        # print(visited)
    return answer

### 2 - 참고 풀이
# https://cocojelly.github.io/algorithm/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%97%B0%EC%8A%B5-DFS-BFS-(2)/
# def solution(n, computers):
#     answer = 0
#     bfs = []
#     visited = [0]*n
#
#     while 0 in visited:
#         bfs.append(visited.index(0))
#         while bfs:
#             node = bfs.pop(0)
#             visited[node] = 1
#             for i in range(n):
#                 if visited[i] == 0 and computers[node][i] == 1:
#                     bfs.append(i)
#         answer += 1
#     return answer


param1 = 3
param2 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(param1, param2))
