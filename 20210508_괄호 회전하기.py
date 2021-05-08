# https://programmers.co.kr/learn/courses/30/lessons/76502

'''
1. 주어진 문자열을 회전시킨다 (cur_s)
2. 괄호 모양에 따라
    2-1. 열리는 괄호일 경우, stack에 추가해준다 ( "(", "[", "{" )
    2-2. 닫히는 괄호일 경우, 스택 top과 짝을 맺을 수 있으면 pop한다
        2-2-1. 짝을 맺을 수 없으면 올바른 괄호 문자열이 아니므로 for문을 멈춘다
3. 온전히 for문을 돌았을 경우 answer에 1을 더해준다
'''

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