for _ in range(int(input())):
    a=1
    h,w,n=map(int,input().split())
    while h<n:
        a+=1
        n-=h
    print(f'{n}{0 if a<10 else ""}{a}')