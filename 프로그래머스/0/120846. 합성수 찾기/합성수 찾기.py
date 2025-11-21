def solution(n):
    # 1. 합성수를 셀 변수
    answer = 0
    
    # 2. 1부터 n번까지 반복문
    for i in range(1, n+1):
        # 3. 1,2,3은 합성수가 아님
        if i < 4:
            continue
        # 4. i의 절반까지를 2부터 반복
        # - 합성수 면 해당 반목문을 멈춤
        for x in range(2, int(i ** 0.5)+1):
            if i % x == 0:
                answer += 1
                break
    
    # 5. 결과를 반환
    return answer