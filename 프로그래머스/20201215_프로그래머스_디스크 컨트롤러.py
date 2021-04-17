def solution(jobs):
    ### 1 - 혼자 풀이
    # 정확성 테스트 20/20
    jobs.sort(key=lambda x:x[0])
    records = []

    time = 0
    while len(jobs) > 0:
        jobs_in_queue = [job for job in jobs if job[0] <= time]
        if len(jobs_in_queue) > 0:
            jobs_in_queue.sort(key=lambda x:x[1])
            records.append([jobs_in_queue[0][0], time+jobs_in_queue[0][1]])
            # print(records)
            jobs.remove(jobs_in_queue[0])
            time += jobs_in_queue[0][1]
        else:
            time += 1

    temp = 0
    for record in records:
        temp += record[1] - record[0]

    return temp // len(records)


param1 = [[1, 9], [0, 3], [2, 6]]
print(solution(param1))
