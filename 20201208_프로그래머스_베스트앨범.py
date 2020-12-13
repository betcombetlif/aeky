def solution(genres, plays):
    ### 1 - 혼자 풀이
    # 정확성 테스트 15/15
    music = {}
    for g, (i, p) in zip(genres, enumerate(plays)):
        if g not in music:
            music[g] = [0, []]
        music[g][0] += p
        music[g][1].append((i, p))

    music_sorted = sorted(music.items(), key=lambda x:x[1][0], reverse=True)
    for m in music_sorted:
        m[1][1] = sorted(m[1][1], key=lambda x:x[1], reverse=True)
    
    answer = []
    for i in range(len(music_sorted)):
        if len(music_sorted[i][1][1]) < 2:
            answer.append(music_sorted[i][1][1][0][0])
        else:
            answer.append(music_sorted[i][1][1][0][0])
            answer.append(music_sorted[i][1][1][1][0])
    
    return answer
