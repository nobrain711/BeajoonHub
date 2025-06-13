def solution(number, k):
    answer = []
    
    for n in number:
        while answer and n > answer[-1] and k > 0:
            answer.pop()
            k -= 1
        answer.append(n)
    
    if k > 0:
        answer = answer[:-k]
        
    answer = ''.join(answer)    
    return answer