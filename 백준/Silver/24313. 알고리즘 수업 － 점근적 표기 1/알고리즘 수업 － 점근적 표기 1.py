a,b=map(int,input().split())
c=int(input())
n=int(input())
r=1 if a*n+b<=c*n and c>=a else 0
print(r)