su=int(input())
l=[]
v=0
for i in range(su):
    a=list(map(int,input().split()))
    l.append(a)
for j in range(len(l)):
    for k in range(len(l)):
        if j==k:
            v+=l[j][k]
print(v)
