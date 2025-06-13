import sys

len_number = int(sys.stdin.readline())
items = [list(sys.stdin.readline().split()) for _ in range(len_number)]

queue = []
for item in items:
  if item[0] == 'push':
    queue.append(item[1])
  elif item[0] == 'pop':
    if len(queue) == 0:
      print(-1)
    else:
      print(queue[0])
      queue.pop(0)
  elif item[0] == 'size':
    print(len(queue))
  elif item[0] == 'empty':
    print(1 if len(queue) == 0 else 0)
  elif item[0] == 'front':
    print(-1 if len(queue) == 0 else queue[0])
  elif item[0] == 'back':
    print(-1 if len(queue) == 0 else queue[-1])