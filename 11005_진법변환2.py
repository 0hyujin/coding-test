system = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" #10진법이면 9 까지, 36진법이면 Z까지 표현된다
N, B = map(int, input().split())
answer = ''

while N != 0:
    answer += str(system[N % B]) #위치로 진법 변환
    N //= B
    
print(answer[::-1])
