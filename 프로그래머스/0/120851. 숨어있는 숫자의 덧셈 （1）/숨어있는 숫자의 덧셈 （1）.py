def solution(my_string):
    return sum(list(int(string) for string in my_string if string.isdigit()))