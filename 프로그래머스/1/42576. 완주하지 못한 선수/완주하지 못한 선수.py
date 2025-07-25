def solution(participant, completion):
    counts = {}
    
    for p in participant:
        counts[p] = counts.get(p,0)+1
    
    for c in completion:
        counts[c] -= 1
    
    for name, cnt in counts.items():
        if cnt > 0:
            return name