# 행렬의 크기
N,M=map(int, input().split())

# 행렬 A
A=[]
for _ in range(N):
    A.append(list(map(int,input().split())))
    
# 행렬 B
B=[]
for _ in range(N):
    B.append(list(map(int,input().split())))

# 정답
for j in range(N):
    for k in range(M):
        print(A[j][k] + B[j][k],end=" ")
    print()