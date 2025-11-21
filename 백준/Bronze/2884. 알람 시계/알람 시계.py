h,m=map(int,input().split())
if(m-45<0):
  print(f'{h-1 if h-1>-1 else 23} {m-45+60}')
else:
  print(f'{h} {m-45}')