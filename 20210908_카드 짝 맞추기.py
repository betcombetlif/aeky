# https://programmers.co.kr/learn/courses/30/lessons/72415

def solution(board, r, c):

    def get_distance(pos_a, pos_b):
        distance = 0
        if abs(pos_a[0] - pos_b[0]) > 0:
            distance += 1
        if abs(pos_a[1] - pos_b[1]) > 0:
            distance += 1
        return distance

    def find_closest_card(i, j, board, pos):
        dir = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        alter = []

        queue = []
        visited = []
        queue.append([i, j])
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.append(node)
                for i in range(4):
                    if 0 <= node[0]+dir[i][0] < 4 and 0 <= node[1]+dir[i][1] < 4:
                        queue.append([node[0]+dir[i][0], node[1]+dir[i][1]])
                        if board[node[0]+dir[i][0]][node[1]+dir[i][1]] > 0:
                            alter.append([node[0]+dir[i][0], node[1]+dir[i][1]])

        answer = []
        min_dis = float('inf')
        for pos in alter:
            print(get_distance([i, j], pos))
            if min_dis > get_distance([i, j], pos):
                min_dis = get_distance([i, j], pos)
                answer = pos
        pos.append(answer)
        return answer

    left = 0
    enter = 0
    for i in range(4):
        for j in range(4):
            if board[i][j] > 0:
                left += 1
                enter += 1

    current = [r, c]
    pos = []
    while left > 0:
        print(current, left)
        for i in range(4):
            for j in range(4):
                if board[i][j] != 0 and board[current[0]][current[1]] != 0:
                    if i != current[0] and j != current[1]:
                        if board[i][j] == board[current[0]][current[1]]:
                            board[current[0]][current[1]] = 0
                            board[i][j] = 0
                            pos.append([(current[0], current[1]), (i, j)])
                            left -= 2
                            current = find_closest_card(i, j, board, pos)

    print(pos)

    answer = 0
    return answer + enter


board = [[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]]
r = 1
c = 0
print(solution(board, r, c))
