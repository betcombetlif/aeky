def solution(citations):
    ### 1 - 혼자 풀이
    # 정확성 테스트 16/16
    citations.sort(reverse=True)
    h_index = citations[len(citations)//2]
    count = len(citations[:len(citations)//2+1])
    while h_index != count:
        count = 0
        for c in citations:
            if c >= h_index:
                count += 1
        # print(h_index, count)
        if h_index > count:
            h_index -= 1
        elif h_index < count:
            h_index += 1
        else:
            break
    return h_index


param1 = [12, 11, 10, 9, 8, 1]
print(solution(param1))