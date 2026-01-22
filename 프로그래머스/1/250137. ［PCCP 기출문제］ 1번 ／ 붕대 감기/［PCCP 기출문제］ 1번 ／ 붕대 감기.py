def solution(bandage, health, attacks):
    t,x,y = bandage
    max_health = health
    max_time = attacks[-1][0]
    health_count = 0
    monster = 0
    for time in range(1, max_time+1):
        if monster != len(attacks) and \
        time == attacks[monster][0]:
            health -= attacks[monster][1]
            health_count = 0
            monster+=1
            
            if health < 1:
                return -1
        elif health == max_health:
            health_count += 1
            if health_count == t:
                health_count = 0
        else:
            health += x
            health_count += 1
            if health_count == t:
                health += y
                health_count = 0
            if health > max_health:
                health = max_health
    return health
            
            