# https://programmers.co.kr/learn/courses/30/lessons/81302
# ㅠㅠ

def solution(places):

    def get_distance(first, second):
        return abs(first[0] - second[0]) + abs(first[1] - second[1])

    def smaller(a, b):
        if a < b:
            return a
        else:
            return b

    def bigger(a, b):
        if a > b:
            return a
        else:
            return b

    answer = []

    for place in places:
        # 한 대기실 내 존재하는 모든 P의 위치 수집
        locations = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    locations.append([i, j])

        flag = True
        for i in range(len(locations)):
            for j in range(i + 1, len(locations)):
                if get_distance(locations[i], locations[j]) <= 2:  # 맨해튼 거리 2 이하일 때
                    # "O" 있는지 확인하는 범위
                    col_start = smaller(locations[i][1], locations[j][1])
                    col_end = bigger(locations[i][1], locations[j][1])
                    row_start = smaller(locations[i][0], locations[j][0])
                    row_end = bigger(locations[i][0], locations[j][0])
                    for k in range(col_start, col_end+1):
                        for t in range(row_start, row_end+1):
                            if place[t][k] == "O": # 파티션으로 막혀있지 않을 경우
                                flag = False
                                break
                        if flag is False:
                            break
                if flag is False:
                    break
            if flag is False:
                break

        if flag is True:
            answer.append(1)
        else:
            answer.append(0)

    return answer


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))

