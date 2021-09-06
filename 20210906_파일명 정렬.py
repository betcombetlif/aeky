# https://programmers.co.kr/learn/courses/30/lessons/17686

def solution(files):
    import re

    file_list = []
    for i in range(len(files)):
        number = re.findall('\d+', files[i])[0]
        head = files[i][:files[i].index(number)].upper()
        file_list.append([files[i], head, int(number), i])

    file_list = sorted(file_list, key=lambda x: (x[1], x[2], x[3]))
    # print(file_list)

    answer = []
    for file in file_list:
        answer.append(file[0])
    return answer


files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))
