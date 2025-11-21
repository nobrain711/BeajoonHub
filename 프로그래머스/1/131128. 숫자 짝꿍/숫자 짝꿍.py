def solution(X, Y):
    # 1. 각 문자열(X, Y)에서 숫자(0~9)의 등장 횟수를 저장할 배열
    count_x = [0] * 10
    count_y = [0] * 10
    
    # 2. X, Y 에서 숫자를 셈
    for x in X:
        count_x[int(x)] += 1
    
    for y in Y:
        count_y[int(y)] += 1
    
    # 3. 두 문자열에서 공통으로 가진 숫자를 큰 숫자부터 결과 문자열로 생성
    #    - 9부터 0까지 순회하면 별도의 정렬 없이 바로 '가장 큰 수' 구성 가능
    #    - 각 숫자의 공통 개수는 min(count_x[i], count_y[i])
    #    - 문자열 곱셈(str(i) * 개수)을 통해 반복 추가
    result = "".join([str(i) * min(count_x[i], count_y[i]) for i in range(9, -1, -1)])
    
    # 4. 공통 숫자가 하나도 없는 경우
    if result == "":
        return '-1'
    
    # 5. 결과가 모두 0으로만 이루어진 경우(예: "0000"), "0"만 반환
    if result[0] == '0':
        return '0'
    
    # 6. 그 외 정상 반환
    return result