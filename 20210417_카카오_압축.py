# https://programmers.co.kr/learn/courses/30/lessons/17684
# 통과

def solution(msg):
    answer = []

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    word_dict = {}
    num = 1
    for letter in alphabet:
        word_dict[letter] = num
        num += 1

    start = 0
    end = start + 1
    while len(msg) > 0:
        # print(start, end)

        current_text = msg[start:end]
        for i in range(len(msg)):
            if msg[start:end+1] in word_dict.keys():
                end += 1
                current_text = msg[start:end]
                continue
            else:
                break

        # print(current_text, word_dict[current_text])

        answer.append(word_dict[current_text])
        if end < len(msg):
            word_dict[current_text + msg[end]] = num
            num += 1

        msg = msg[end:]
        end = start + 1

    return answer


msg = "TOBEORNOTTOBEORTOBEORNOT"
print(solution(msg))
