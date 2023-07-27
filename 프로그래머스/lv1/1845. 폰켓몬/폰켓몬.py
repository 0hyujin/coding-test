def solution(nums):
    choose = int(len(nums) / 2) # 주어지는 리스트는 항상 짝수
    nums = set(nums) # set으로 중복 제거
    
    answer = min(len(nums), choose)
    
    return answer