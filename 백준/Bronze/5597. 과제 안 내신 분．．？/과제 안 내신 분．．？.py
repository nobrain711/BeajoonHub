s=[i for i in range(1,31)]

for _ in range(28):
    i = int(input())
    s.remove(i)
s.sort()
print(*s,sep="\n")