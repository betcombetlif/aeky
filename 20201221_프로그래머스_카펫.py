def solution(brown, yellow):
    ### 1 - 혼자 풀이
    # 정확성 테스트 13/13
    yellow_yaksu = []
    for i in range(1, yellow+1):
        if yellow % i == 0:
            temp = [i, yellow//i]
            temp.sort(reverse=True)
            if temp not in yellow_yaksu:
                yellow_yaksu.append(temp)

    yelbro_yaksu = []
    for i in range(2, (yellow+brown)//2):
        if (yellow+brown) % i == 0:
            temp = [i, (yellow+brown)//i]
            temp.sort(reverse=True)
            if temp not in yelbro_yaksu:
                yelbro_yaksu.append(temp)

    print(yellow_yaksu, yelbro_yaksu)
    answer = []
    for [x, y] in yelbro_yaksu:
        if [x-2, y-2] in yellow_yaksu:
            answer.append(x)
            answer.append(y)

    return answer


param1 = 8
param2 = 1
print(solution(param1, param2))
