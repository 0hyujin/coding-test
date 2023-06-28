def solution(이름, 점수, 사진):
    return [sum(점수[이름.index(사람)] 
                for 사람 in 사람들 
                if 사람 in 이름) 
            for 사람들 in 사진]