su=input()
l=list(map(int,input().split()))
l1=[]
for i in l:
    l1.append(l.count(i))
b=max(l1)
c=l1.index(b)
print(l[c])
