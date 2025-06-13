N = int(input())
input_str = []

for _ in range(N):
  input_str.append(input())

input_str = set(input_str)
input_str = list(input_str)
input_str.sort()
input_str.sort(key=len)

for i in input_str:
  print(i)