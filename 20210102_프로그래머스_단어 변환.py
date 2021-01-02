### 1 - 혼자 풀이
# 정확성 테스트 5/5
def check_difference(str1, str2):
    count = 0
    for a, b in zip(str1, str2):
        if a != b:
            count += 1
    return count


def solution(begin, target, words):
    if target not in words:
        return 0

    answer = 0
    current = ''.join(begin)
    stack = []
    visited = [False] * len(words)
    while current != target:
        for word in words:
            if check_difference(current, word) == 1:
                stack.append(word)
        while stack:
            if current == target:
                return answer
            current = stack.pop()
            visited[words.index(current)] = True
            answer += 1
            for i in range(len(words)):
                if visited[i] is False and words[i] not in stack and check_difference(current, words[i]) == 1:
                    stack.append(words[i])

    return answer


### 2 - 참고 풀이
# https://nyeongnyeong.tistory.com/m/66


param1 = "hit"
param2 = "cog"
param3 = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(param1, param2, param3))
