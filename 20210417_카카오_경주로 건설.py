# https://programmers.co.kr/learn/courses/30/lessons/67259

# def solution(board):
#     LINE_COST = 100
#     CORNER_COST = 500
#
#     cord_x = 0
#     cord_y = 0
#     n = len(board)
#     answer = 0
#
#     def recursion(cord_x, cord_y, answer):
#         if cord_x == n - 1 and cord_y == n - 1:
#             return answer
#
#         if board[cord_x][cord_y+1] == 0: # 상
#             answer += recursion(cord_x, cord_y+1)
#         elif board[cord_x][cord_y-1] == 0: # 하
#             answer += recursion(cord_x, cord_y-1)
#         elif board[cord_x-1][cord_y] == 0: # 좌
#             answer += recursion(cord_x-1, cord_y)
#         elif board[cord_x+1][cord_y] == 0: # 우
#             answer += recursion(cord_x+1, cord_y)
#
#     answer = recursion(cord_x, cord_y, answer)
#
#     return answer
#
#
# board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# print(solution(board))

# 참고 코드 https://m.blog.naver.com/hands731/222064903541

from collections import deque


def solution(board):
    n = len(board)
    x = [0, 1, 0, -1]
    y = [1, 0, -1, 0]
    visited = [[-1] * n for _ in range(n)]
    visited[0][0] = 0
    que = deque()
    que.append((0, 0, 0, 0))  # (0,0)에서 (0,1)과 (1,0)으로 가는 경우 두개를 큐에 넣는다.
    que.append((0, 0, 0, 1))
    while que:
        value, i, j, k = que.popleft()
        for z in range(4):
            nx = i + x[z]
            ny = j + y[z]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if board[nx][ny] == 1:
                continue
            cost = 100 if k == z else 600
            news = value + cost
            if visited[nx][ny] == -1 or news <= visited[nx][ny]:
                visited[nx][ny] = news
                que.append((news, nx, ny, z))
    return visited[n - 1][n - 1]
