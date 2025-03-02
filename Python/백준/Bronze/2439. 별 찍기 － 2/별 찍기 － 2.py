r=int(input())+1
for i in range(1,r):
    for _ in range(1,r-i):
        print(end=' ')
    print('*'*i)