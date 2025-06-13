import sys

numbers = []

input_count = int(sys.stdin.readline())

for _ in range(input_count):
  numbers.append(int(sys.stdin.readline()))

numbers.sort()
for number in numbers:
  print(number) 