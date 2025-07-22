def solution(sides):
    a,b,c=sides
    return (1 if(a+b>c and b+c>a and a+c>b) else 2)