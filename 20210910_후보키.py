# https://programmers.co.kr/learn/courses/30/lessons/42890
# 참고: https://codlingual.tistory.com/161

def solution(relation):
    from itertools import combinations

    N = len(relation[0])  # 속성의 개수
    key_idx = list(range(N))
    candidate_keys = []

    for i in range(1, N+1):
        for comb in combinations(key_idx, i):
            print(comb)
            hist = []
            for rel in relation:
                current_key = [rel[c] for c in comb]

                if current_key in hist:  # 하나라도 중복되는 경우: 식별 불가능
                    break
                else:
                    hist.append(current_key)

            else:  # 하나도 중복 안 된 경우: 식별 가능
                for ck in candidate_keys:
                    print("HERE> ", ck)
                    print(set(ck))
                    print(set(comb))
                    if set(ck).issubset(set(comb)):  # 최소성 확인
                        break
                else:
                    print("check")
                    candidate_keys.append(comb)

    return len(candidate_keys)


relation = [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
            ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]
print(solution(relation))
