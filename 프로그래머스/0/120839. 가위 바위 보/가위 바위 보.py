def solution(rsp):
    # 가위 2>5
    # 바위 0>2
    # 보   5>0
    answer = []
    for i in rsp:
        if i == '2':
            answer.append('0')
        elif i == '0':
            answer.append('5')
        elif i == '5':
            answer.append('2')
    return ''.join(a for a in answer)