def solution(price, money, count):
    # 등차 수열이용해서 전체가격을 구한 후 현재 금액에서 가격을 계산
    # max로 0보다 큰 금액은 그냥 반환금액이 0이 보다 작으면 0반환
    return max(0, price*(count+1)*count//2 - money)