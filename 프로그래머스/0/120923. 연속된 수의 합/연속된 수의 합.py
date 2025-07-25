def solution(num, total):
    answer = [i for i in range(num)]
    while True:
        if sum(answer)==total:
            return answer
        elif sum(answer)<total:
            answer=[i+1 for i in answer]
        elif sum(answer)>total:
            answer=[i-1 for i in answer]