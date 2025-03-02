while 1:
    a,b,c=map(int,input().split())
    if(a==0 and b==0 and c==0):
        break
    print('right' if ((a*a)+(b*b)==c*c) or ((b*b)+(c*c)==a*a) or ((a*a)+(c*c)==b*b) else 'wrong')