def solution(array):
    # 1. 숫자를 세기 위한 list생성
    # - 1001를 곱하는 이유는 array의 최대 원소 갯수
    idx = [0] * 1001
    
    # 2. array를 반복문에 넣어서 숫자를 셈
    for item in array:
        idx[item] += 1
        
    # 3. 가장 많은 숫자를 찾기아서 반환
    # - 가장 많은 숫자가 1개를 초과하면 -1를 반환
    if idx.count(max(idx)) > 1:
        return -1
    
    return idx.index(max(idx))