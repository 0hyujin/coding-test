a,b = input().split()
a = int(a[::-1])  # [::-1] : 역순
b = int(b[::-1])

if a > b:
    print(a)
else :
    print(b)
