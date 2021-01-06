### 1 - 혼자 풀이
# 시간 초
def dfs(start, size, graph):
    visited = [False] * size
    stack = [start]
    while False in visited:
        while stack:
            current = stack.pop()
            if visited[current - 1] is False:
                visited[current - 1] = True
                print(current, end=" ")
            for node in sorted(graph[current], reverse=True):
                if visited[node - 1] is False:
                    stack.append(node)


def bfs(start, size, graph):
    visited = [False] * size
    queue = [start]
    while False in visited:
        while queue:
            current = queue.pop(0)
            if visited[current - 1] is False:
                visited[current - 1] = True
                print(current, end=" ")
            for node in sorted(graph[current]):
                if visited[node - 1] is False:
                    queue.append(node)


from collections import defaultdict

n, m, v = map(int, input().split())
connected = defaultdict(list)
for i in range(m):
    a, b = map(int, input().split())
    connected[a].append(b)
    connected[b].append(a)
# print(n, m, v, connected)
dfs(v, n, connected)
print()
bfs(v, n, connected)


### 2 - 참고 풀이
# https://pacific-ocean.tistory.com/260
# def dfs(v):
#     print(v, end=' ')
#     visit[v] = 1
#     for i in range(1, n + 1):
#         if visit[i] == 0 and s[v][i] == 1:
#             dfs(i)
#
#
# def bfs(v):
#     queue = [v]
#     visit[v] = 0
#     while (queue):
#         v = queue[0]
#         print(v, end=' ')
#         del queue[0]
#         for i in range(1, n + 1):
#             if visit[i] == 1 and s[v][i] == 1:
#                 queue.append(i)
#                 visit[i] = 0
#
#
# n, m, v = map(int, input().split())
# s = [[0] * (n + 1) for i in range(n + 1)]
# visit = [0 for i in range(n + 1)]
# for i in range(m):
#     x, y = map(int, input().split())
#     s[x][y] = 1
#     s[y][x] = 1
#
# dfs(v)
# print()
# bfs(v)
