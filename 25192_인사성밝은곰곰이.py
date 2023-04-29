N=int(input())

dic={}

cnt=0

for _ in range(N):
    Input=input()

    if Input=="ENTER":
        for key,value in dic.items():
            if value==1:
                cnt+=1
        dic={}
    else:
        if Input not in dic:
            dic[Input]=1

for key,value in dic.items():
    if value==1:
        cnt+=1

print(cnt)
