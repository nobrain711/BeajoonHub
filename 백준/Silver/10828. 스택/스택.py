import sys
number = int(sys.stdin.readline())
items = [list(sys.stdin.readline().split()) for _ in range(number)]

stack = []

for item in items:
  if item[0] == 'push':
    stack.append(item[1])
  elif item[0] == 'pop':
    print(-1 if len(stack) == 0 else stack.pop())
  elif item[0] == 'size':
    print(len(stack))
  elif item[0] == 'empty':
    print(1 if len(stack) == 0 else 0)
  elif item[0] == 'top':
    print(-1 if len(stack) == 0 else stack[-1])