grade = str(input())

if len(grade) > 1:    
    main = grade[0]
    sub = grade[1]
    
    score = 0

    if main == 'A':
        score = 4.0
        if sub == '+':
            score += 0.3
        if sub == '-':
            score -= 0.3

    elif main == 'B':
        score = 3.0
        if sub == '+':
            score += 0.3
        if sub == '-':
            score -= 0.3

    elif main == 'C':
        score = 2.0
        if sub == '+':
            score += 0.3
        if sub == '-':
            score -= 0.3

    else:
        score = 1.0
        if sub == '+':
            score += 0.3
        if sub == '-':
            score -= 0.3

    print(score)

else:
    print(0.0)
