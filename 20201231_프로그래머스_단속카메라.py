### 1 - 혼자 풀이
# 풀이 방법을 떠올리지 못함...
def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    answer = 0
    return answer

### 2 - 참고 풀이
# https://wwlee94.github.io/category/algorithm/greedy/speed-enforcement-camera/


param1 = [[-20, 15], [-14, -5], [-18, -13], [-5, -3]]
print(solution(param1))
