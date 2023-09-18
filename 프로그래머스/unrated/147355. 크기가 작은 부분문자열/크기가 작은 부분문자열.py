def solution(t, p):
    answer = 0
    
    lenT = len(t)
    lenP = len(p)
    p = int(p)
    for i in range (0, lenT - lenP + 1):
        if int(t[i:i+lenP]) <= p:
              answer+=1
    return answer