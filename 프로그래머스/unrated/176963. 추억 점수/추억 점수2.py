def solution(name, yearning, photo):
    answer = [] 
    for people in photo: 
        score = 0 
        for person in people: 
            if person in name: 
                idx = name.index(person)
                score += yearning[idx] 
        answer.append(total_score) 
    return answer 
