# https://programmers.co.kr/learn/courses/30/lessons/76502

def solution(s):
    answer = 0
    size = len(s)

    open = ["(", "[", "{"]

    for i in range(size):
        cur_s = s[i:] + s[:i]

        stack = []
        flag = True
        for j in range(size):
            if cur_s[j] in open:
                stack.append(cur_s[j])
            else: # close일 경우
                if len(stack) > 0:
                    top = stack[-1]
                    if cur_s[j] == ")" and top == "(":
                        stack.pop()
                    elif cur_s[j] == "]" and top == "[":
                        stack.pop()
                    elif cur_s[j] == "}" and top == "{":
                        stack.pop()
                    else:
                        flag = False
                        break
                else:
                    flag = False
                    break

        if flag is True and len(stack) == 0:
            answer += 1

    return answer


s = "{{{{{{{{{{"
print(solution(s))