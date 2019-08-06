a=input()
su=list(input().split())
l=[]
for i in su:
    l.append(i.lower())
l=sorted(l)
for j in l:
    print(j)
