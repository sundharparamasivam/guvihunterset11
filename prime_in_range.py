su=int(input())
l=[]
if su<=2:
    print(0)
if su>2:
    for i in range (2,su):
        c=1
        for j in range(2,i):
            if i%j==0:
                c+=1
        if c==1:
            l.append(i)
print(*l)
