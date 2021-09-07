# https://programmers.co.kr/learn/courses/30/lessons/72414
# 참고: https://cocook.tistory.com/133

def solution(play_time, adv_time, logs):
    def time_to_int(time):
        h_m_s = time.split(":")
        hour = int(h_m_s[0]) * 60 * 60
        minute = int(h_m_s[1]) * 60
        second = int(h_m_s[2])
        return hour + minute + second

    def int_to_time(number):
        second = "0" + str(number % 60)
        minute = "0" + str(number // 60 % 60)
        hour = "0" + str(number // 60 // 60)
        return hour[-2:] + ":" + minute[-2:] + ":" + second[-2:]


    play_time = time_to_int(play_time)
    adv_time = time_to_int(adv_time)
    clock = [0] * (play_time + 1)

    for log in logs:
        start, end = log.split("-")
        clock[time_to_int(start)] += 1
        clock[time_to_int(end)] -= 1

    # 각 시점별 재생횟수 구하기
    for i in range(1, play_time + 1):
        clock[i] = clock[i] + clock[i-1]

    # 각 시점별 재생횟수의 누적합 = 누적 재생횟수
    for i in range(1, play_time + 1):
        clock[i] = clock[i] + clock[i-1]

    # 00:00:00부터 play_time까지 누적 합의 최댓값을 리턴하는 초를 찾기
    answer = 0
    current_max = clock[adv_time]  # 기본 값: 00:00:00부터 시작했을 때의 누적 합
    for start in range(1, play_time):
        if start + adv_time < play_time:
            end = start + adv_time
        else:
            end = play_time

        temp = clock[end] - clock[start]
        if current_max < temp:
            current_max = temp
            answer = start + 1
    return int_to_time(answer)


play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

print(solution(play_time, adv_time, logs))
