def solution(arr):
    answer = []
    
    for item in arr:
        if answer[-1:] != [item]:
            answer.append(item)
            
    return answer