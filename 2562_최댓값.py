numbers=[]            #배열 선언
for _ in range(9):    #range(0,9)랑 같음 0, 1, ..., 8
                      #range(stop) stop은 제외 -> 총 9개
    a = int(input())  #입력 받음
    numbers.append(a) #배열에 a 삽입
    
# numbers=list(map(int, input().split())) 
# 이렇게 하면 숫자를 나열하고 엔터 쳐야함
# 위 코드는 숫자 하나씩 입력하고 엔터
    
print(max(numbers))
print(numbers.index(max(numbers))+1)

#예전에 푼거 복습
