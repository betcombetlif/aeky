# https://programmers.co.kr/learn/courses/30/lessons/72413

def solution(n, s, a, b, fares):

    def get_closest_node(distance, visited):
        min_value = MAX
        index = 0
        for i in range(1, n+1):
            if distance[i] < min_value and not visited[i]:
                min_value = distance[i]
                index = i
        return index

    def dijkstra(start):
        distance = [MAX] * (n+1)
        visited = [False] * (n+1)

        distance[start] = 0
        visited[start] = True

        for j in graph[start]:
            distance[j[0]] = j[1]

        for i in range(n-1):
            current = get_closest_node(distance, visited)
            visited[current] = True
            for j in graph[current]:
                cost = distance[current] + j[1]
                if cost < distance[j[0]]:
                    distance[j[0]] = cost

        return distance

    MAX = float('inf')
    graph = [[] for _ in range(n+1)]

    for fare in fares:
        graph[fare[0]].append([fare[1], fare[2]])
        graph[fare[1]].append([fare[0], fare[2]])

    from_s = dijkstra(s)
    min_fare = from_s[a] + from_s[b]
    # print(from_s[1:])

    for i in range(1, n+1):
        from_i = dijkstra(i)
        # print(i, from_i[1:])
        temp = from_s[i] + from_i[a] + from_i[b]
        if temp < min_fare:
            min_fare = temp

    return min_fare


n = 7
s = 3
a = 4
b = 1
fares = [[3, 4, 9], [4, 6, 100000], [3, 6, 1], [3, 2, 100000], [2, 1, 6]]
print(solution(n, s, a, b, fares))