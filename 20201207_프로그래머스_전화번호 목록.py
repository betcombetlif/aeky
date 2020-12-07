def solution(phone_book):
    ### 1 - 혼자 풀이
    # 정확성 테스트 11/11, 효율성 테스트 0/2
    answer = True
    
    hash_map = {}
    for i in range(1,10):
        hash_map[str(i)] = []
    
    for pb in phone_book:
        if len(hash_map[pb[0]]) == 0:
            hash_map[pb[0]].append(pb)
        else:
            for n in hash_map[pb[0]]:
                if pb == n[:len(pb)] or n == pb[:len(n)]:
                    answer = False
                    break
            hash_map[pb[0]].append(pb)
    
    return answer

    ### 2 - 참고 풀이
    # phone_book.sort()
    # for p1, p2 in zip(phone_book, phone_book[1:]):
    #     if p2.startswith(p1):
    #         return False
    # return True