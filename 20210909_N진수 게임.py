# https://programmers.co.kr/learn/courses/30/lessons/17687

def solution(n, t, m, p):
    def convert(n, base):
        T = "0123456789ABCDEF"
        q, r = divmod(n, base)
        if q == 0:
            return T[r]
        else:
            return convert(q, base) + T[r]

    cur_num = 0
    count = 0
    numbers = ''
    while count < t * m:
        conv_num = convert(cur_num, n)
        numbers += conv_num
        cur_num += 1
        count += len(conv_num)
    # print(numbers)

    answer = ''
    idx = p-1
    while t:
        answer += numbers[idx]
        idx += m
        t -= 1

    return answer


n = 16
t = 16
m = 2
p = 1
print(solution(n, t, m, p))