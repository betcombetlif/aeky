def solution(participant, completion):
    ### 1 - 혼자 풀이
    # 정확성 테스트 5/5, 효율성 테스트 0/5
    for c in completion:
        if c in participant:
            participant.remove(c)
    return participant[0]

    ### 2 - 참고 풀이
    # 정확성 테스트 5/5, 효율성 테스트 5/5
    # participant.sort()
    # completion.sort()
    
    # for p, c in zip(participant, completion):
    #     if p != c:
    #         return p
    # return participant[-1]