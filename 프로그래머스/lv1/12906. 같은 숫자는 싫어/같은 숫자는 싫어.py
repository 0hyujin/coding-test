def solution(arr):
    answer=[]
    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
        elif arr[i] != arr[i-1]: # 만약 현재 list의 값이 그 전의 값과 다르다면
            answer.append(arr[i]) # answer list에 추가
    return answer