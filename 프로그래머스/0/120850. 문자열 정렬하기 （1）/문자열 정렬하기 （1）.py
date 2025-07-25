def solution(my_string):
    number = [str(i) for i in range(10)]
    return sorted([int(string) for string in my_string if string in number])