def solution(scoville, K):
    ### 1 - 혼자 풀이
    # 정확성 테스트 16/16, 효율성 테스트 5/5
    import heapq
    heapq.heapify(scoville)
    count = 0
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        heapq.heappush(scoville, min1 + (2*min2))
        count += 1
    return count

param1= [1, 2, 3, 9, 10, 12]
param2 = 7
print(solution(param1, param2))