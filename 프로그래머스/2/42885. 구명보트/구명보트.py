def solution(people, limit):
    answer = 0
    people = sorted(people, reverse=True)
    
    for p in people:
        if p + people[-1] <= limit:
            print(p + people[-1])
            people.pop()
            
        answer += 1
    
    return answer