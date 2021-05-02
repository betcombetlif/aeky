# https://programmers.co.kr/learn/courses/30/lessons/42861

def solution(n, costs):
    answer = 0

    costs = sorted(costs, key=lambda x: x[2])
    print(costs)
    selected = 0
    unified = [i for i in range(n)]

    def get_root(x):
        if unified[x] == x:
            return x
        else:
            return get_root(unified[x])

    i = 0
    while selected < n - 1 or i < len(costs):
        print("======")
        if get_root(costs[i][0]) != get_root(costs[i][1]):
            answer += costs[i][2]
            selected += 1
            unified[get_root(costs[i][0])] = costs[i][1]
        i += 1
        print(selected, unified)

    return answer


n = 6
costs = [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]]
print(solution(n, costs))


# 참고 풀이
# https://programmers.co.kr/learn/courses/30/lessons/42861/solution_groups?language=python3
#
# def ancestor(node, parents):
#     if parents[node] == node:
#         return node
#     else:
#         return ancestor(parents[node], parents)
#
# def solution(n, costs):
#     answer = 0
#     edges = sorted([(x[2], x[0], x[1]) for x in costs])
#     parents = [i for i in range(n)]
#     bridges = 0
#     for w, f, t in edges:
#         if ancestor(f, parents) != ancestor(t, parents):
#             answer += w
#             parents[ancestor(f, parents)] = t
#             bridges += 1
#         if bridges == n - 1:
#             break
#     return answer
