import sys

n = int(sys.stdin.readline().rstrip('\n'))
cnt = 0
title = 666
now_title = 0

while cnt < n:
    if '666' in str(title):
        cnt += 1
        now_title = title
    title += 1
    
print(now_title)