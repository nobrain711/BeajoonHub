def solution(people, limit):
    boat = 0
    people.sort(reverse=True)
    
    for i in people:
        total = i
        
        if total + people[-1] <= limit: 
            people.pop()
        
        boat += 1
        
    return boat