# https://programmers.co.kr/learn/courses/30/lessons/81303
# ㅠㅠ


def solution(n, k, cmd):
    answer = ['O'] * n
    del_history = []

    def last_row(table):
        for i in range(n-1, 0, -1):
            if table[i] == 'O':
                return i

    current = k
    for c in cmd:
        if c[0] == "U":  # up
            count = int(c[2])
            while count > 0:
                if answer[current-1] == 'X':
                    current = current - 1
                else:
                    current = current - 1
                    count = count - 1
        elif c[0] == "D":  # down
            count = int(c[2])
            while count > 0:
                if answer[current] == 'X':
                    current = current + 1
                else:
                    current = current + 1
                    count = count - 1
        elif c[0] == "C": # delete and choose down
            last = last_row(answer)
            answer[current] = 'X'
            del_history.append(current)
            if current == last:
                current = current - 1
                while answer[current] == 'X':
                    current = current - 1
            else:
                current = current + 1
                while answer[current] == 'X':
                    current = current + 1
        elif c[0] == "Z": # ctrl + Z
            answer[del_history.pop()] = 'O'

        print(c, answer, current)
    return ''.join(answer)


n = 8
k = 2
cmd = ["D 5", "C", "U 3", "C", "D 2", "C", "U 2", "Z", "Z", "U 1", "C"]
print(solution(n, k, cmd))