def solution(my_string):
    answer = ''
    string = list(my_string)[::-1]
    for s in string:
        answer+=s
    return answer