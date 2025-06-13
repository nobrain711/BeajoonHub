a=int(input())
b=int(input())
c=int(input())

number = a*b*c
numbers = [int(i) for i in str(number)]
count_number=0
for i in range(10):
  count=0
  for n in numbers:
    if i == n :
      count += 1

  print(count)