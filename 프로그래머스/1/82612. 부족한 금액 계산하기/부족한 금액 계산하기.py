def solution(price, money, count):
    # 1. 총 가격을 계산
    total_price = sum([i * price for i in range(1, count + 1)])
    
    # 2. 부족한 금액 계산
    answer = total_price - money
    
    # 3. 갔고 있는 금액이 많으면 answer를 0으로 변경
    if answer < 1:
        answer = 0
    
    # 4. answer를 반환
    return answer