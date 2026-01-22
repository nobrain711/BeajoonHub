import sys
cnt = int(sys.stdin.readline())
for _ in range(cnt):
    test=sys.stdin.readline().rstrip('\n')
    print(f'{test[0]}{test[-1]}')