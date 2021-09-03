# https://programmers.co.kr/learn/courses/30/lessons/17683

def solution(m, musicinfos):
    m = m.replace("C#", "H").replace("D#", "I").replace("F#", "J").replace("G#", "K").replace("A#", "L")

    for i in range(len(musicinfos)):
        musicinfos[i] = musicinfos[i].split(",")
        musicinfos[i][3] = musicinfos[i][3].replace("C#", "H").replace("D#", "I").replace("F#", "J").replace("G#", "K").replace("A#", "L")

    answer_list = []
    for music in musicinfos:  # 0 음악이 시작한 시각, 1 끝난 시각, 2 음악 제목, 3 악보 정보
        start_time = list(map(int, music[0].split(":")))
        end_time = list(map(int, music[1].split(":")))
        play_time = (end_time[0] - start_time[0])*60 + end_time[1] - start_time[1]
        played = music[3] * (play_time // len(music[3])) + music[3][:(play_time % len(music[3]))]

        print("> 재생된 음악: ", played)
        print("> 네오가 기억하는 음악: ", m)
        if m in played:
            answer_list.append([music[2], play_time, musicinfos.index(music)])

    if answer_list:
        return sorted(answer_list, key=lambda x: (x[1], -x[2]))[-1][0]
    return "(None)"


m = "ABC"
musicinfos = ["12:00,12:05,HELLO,ABCDEF", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos))