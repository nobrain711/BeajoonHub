def solution(progresses, speeds):
    answer = []
    count = 0
    day = 0
    
    while len(progresses):
        if (progresses[0] + speeds[0] * day) >= 100:
            count += 1
            progresses.pop(0)
            speeds.pop(0)
            
        else:
            if count > 0:
                answer.append(count)
                count = 0
            else:
                day += 1
    answer.append(count)
    return answer