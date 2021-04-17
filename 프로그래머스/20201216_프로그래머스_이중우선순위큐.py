def solution(operations):
    ### 1 - 혼자 풀이
    # 정확성 테스트 6/6
    import heapq
    queue = []
    heapq.heapify(queue)

    for op in operations:
        operator, number = op.split()[0], int(op.split()[1])
        if operator == "I":
            heapq.heappush(queue, number)
        else:
            if len(queue) != 0:
                if number == -1: # 최솟값 삭제
                    heapq.heappop(queue)
                else: # 최댓값 삭제
                    queue.remove(max(queue))
        # print(queue)

    if len(queue) == 0:
        return [0,0]

    return [max(queue), queue[0]]


param1 = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(solution(param1))
