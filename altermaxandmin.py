su=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(len(l)):
    if i%2==0:
        l1.append(max(l))
        l.remove(max(l))
    else:
        l1.append(min(l))
        l.remove(min(l))
print(*l1)
