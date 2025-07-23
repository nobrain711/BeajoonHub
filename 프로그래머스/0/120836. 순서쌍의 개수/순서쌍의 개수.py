def solution(n):
    answer=0
    for i in range(1, int(n**0.5)+1):
        answer+=0 if n%i!=0 else 1 if i == n // i else 2
    return answer