su=list(input().split())
l1=su[0]
l2=su[1]
a=abs(len(l1)-len(l2))
if len(l1)>len(l2):
    for i in range(1,a+1):
        l2+=str(i)
else:
    for i in range(1,a+1):
        l1+=str(i)
l3=[]
for j in range(len(l1)):
    l3.append(l1[j])
    l3.append(l2[j])
print("".join(l3))
