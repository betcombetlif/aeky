### 1 - 혼자 풀이
# direction 수정, visited False -> 0으로 수정

N, M = map(int, input().split())
miro = []
for n in range(N):
    temp = input()
    miro.append([])
    for t in temp:
        miro[n].append(t)

queue = [[0, 0]]
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1
direction = [[0, -1], [0, 1], [1, 0], [-1, 0]] # 좌, 우, 상, 하

while queue:
    current = queue.pop(0)
    if current == [N - 1, M - 1]:
        print(visited[N - 1][M - 1])
        break
    for i in range(4):
        if 0 <= current[0] + direction[i][0] < N and 0 <= current[1] + direction[i][1] < M:
            if miro[current[0] + direction[i][0]][current[1] + direction[i][1]] == '1' and \
                    visited[current[0] + direction[i][0]][current[1] + direction[i][1]] == 0:
                visited[current[0] + direction[i][0]][current[1] + direction[i][1]] = visited[current[0]][current[1]] + 1
                queue.append([current[0] + direction[i][0], current[1] + direction[i][1]])


### 2 - 참고 풀이
# https://chancoding.tistory.com/64