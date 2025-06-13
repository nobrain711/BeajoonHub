def solution(n, lost, reserve):
    answer = 0
    # lost reserve의 중복제거
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)
    
    # 학생 빌려 주기
    for s in reserve_set:
        if s - 1 in lost_set:
            lost_set.remove(s - 1)
        elif s + 1 in lost_set:
            lost_set.remove(s + 1)
    
    # 체육활동이 가능한 학생의 수
    answer = n - len(lost_set)

    return answer