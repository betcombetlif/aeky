### 1 - 혼자 풀이
# 정확성 테스트 11/11
def count_A(name, point_from):
    count = 0
    while True:
        if name[point_from] != 'A':
            break
        else:
            count += 1
        point_from += 1
    return count


def solution(name):
    answer = 0
    name = list(name)
    current = ['A' for _ in range(len(name))]
    alphabet = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
                'M': 12,
                'N': 13, 'O': 12, 'P': 11, 'Q': 10, 'R': 9, 'S': 8, 'T': 7, 'U': 6, 'V': 5, 'W': 4, 'X': 3, 'Y': 2,
                'Z': 1}
    pointer = 0
    last = True
    if current == name:
        return answer
    while current != name:
        if current[pointer] != name[pointer]:
            current[pointer] = name[pointer]
            answer += alphabet[name[pointer]]
        # print(current, name, name[pointer], answer)
        if last is False or (pointer+1 < len(name) and count_A(name, pointer+1) >= pointer+1):
            pointer -= 1
            last = False
        else:
            pointer += 1
        answer += 1
    return answer - 1


### 2 - 참고 풀이
# https://jgrammer.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A1%B0%EC%9D%B4%EC%8A%A4%ED%8B%B1
# def solution(name):
#     make_name = [min(ord(i) - ord("A"), ord("Z") - ord(i)+1) for i in name]
#     idx, answer = 0, 0
#     while True:
#         answer += make_name[idx]
#         make_name[idx] = 0
#         if sum(make_name) ==0:
#             break
#         left, right = 1, 1
#         while make_name[idx - left] ==0:
#             left +=1
#         while make_name[idx + right] ==0:
#             right +=1
#         answer += left if left < right else right
#         idx += -left if left < right else right
#     return answer


param1 = "JEROEN"
print(solution(param1))
