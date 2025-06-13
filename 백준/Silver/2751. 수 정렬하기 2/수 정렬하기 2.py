import sys

input_count = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(input_count)]

numbers.sort()
for number in numbers:
  print(number) 