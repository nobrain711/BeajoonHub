def solution(sides):
    sides.sort()
    max_side=sides.pop()
    sum_sides=sum(sides)
    return (1 if max_side<sum_sides else 2)