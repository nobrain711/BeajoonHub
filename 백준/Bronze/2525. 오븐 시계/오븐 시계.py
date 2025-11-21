h,m=map(int,input().split())
m+=int(input())
print(f'{h+m//60 if h+m//60<24 else (h+m//60)-24} {m%60}')