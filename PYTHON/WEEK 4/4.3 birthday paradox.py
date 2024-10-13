import random
l=[]
for i in range(30):
    l.append(random.randint(1,366))
l.sort()
print(l)


i=0
flage=0
while(i<len(l)-1):
    if (l[i]==l[i+1]):
        print("repeat")
        flage=1
        break
    i=i+1
if flage==0:
    print("there is no repeatation")
    
    