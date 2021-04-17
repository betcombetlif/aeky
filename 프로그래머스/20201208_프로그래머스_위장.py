def solution(clothes):
    ### 1 - 혼자 풀이
    # 정확성 테스트 27/28
    from itertools import combinations
    closet = {}
    for cloth in clothes:
        if cloth[1] not in closet:
            closet[cloth[1]] = 0
        closet[cloth[1]] += 1
    
    answer = 0
    cloth_type = closet.keys()
    for i in range(1, len(closet)+1):
        for combi in combinations(cloth_type, i):
            temp = closet[combi[0]]
            for i in range(1, len(combi)):
                temp *= closet[combi[i]]
            answer += temp
    
    return answer

    ### 2 - 참고 풀이
    # 정확성 테스트 28/28
    # from collections import Counter
    
    # closet = Counter([cloth_type for _, cloth_type in clothes])
    # possibility = 1
    
    # for cloth_type in closet:
    #     possibility *= (closet[cloth_type] + 1)
        
    # return possibility - 1