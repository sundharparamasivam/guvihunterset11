su=input()
b=su+su[0]
a=0
j=0
for i in range(len(su)):
    a+=int(b[j])**int(b[j+1])
    j+=1
print(a)
