S = str(input())
result = ''

for s in S:
    if s.islower():
        result += s.upper()
    else:
        result += s.lower()
        
print(result)