su=input()
l=[]
c=1
for i in su:
    if i==" ":
        l.append(i)
    elif c%2!=0:
        l.append(i.upper())
        c+=1
    else:
        l.append(i.lower())
        c+=1
print("".join(l))
