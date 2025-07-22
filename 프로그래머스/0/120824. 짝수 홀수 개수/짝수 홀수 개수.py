def solution(num_list):
    # 홀수, 짝수 카운트 변수생성
    even=0
    odd=0
    # num_list의 값에서 홀수, 짝수 구분 후에 카운트
    for i in num_list:
        if i%2==0:
            even+=1
        else:
            odd+=1
    # 짝수, 홀수의 카운트를 list로 반환
    return [even, odd]