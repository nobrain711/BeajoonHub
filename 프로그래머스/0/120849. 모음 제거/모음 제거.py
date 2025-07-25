def solution(my_string):
    return ''.join(s for s in my_string if s not in ['a','e','i','o','u'])