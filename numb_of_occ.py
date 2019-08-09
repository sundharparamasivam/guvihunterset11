su=list(map(int,input().split()))
c=0
for i in range(su[0],su[1]):
    if str(su[2]) in str(i):
        c+=1
print(c)
