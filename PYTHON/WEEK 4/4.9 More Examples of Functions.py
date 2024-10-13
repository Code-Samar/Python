def List_min(l):
    mini=l[0]
    for i in range(len(l)):
        if (l[i]<mini):
            mini=l[i]
    return mini        


def List_Max(l):
    maxi=l[0]
    for i in range (len(l)):
        if (l[i]>maxi):
            maxi=l[i]
    return maxi        

def List_appendbefore(l,z):
    newL=[]
    for i in range (len(z)):
        newL.append(z[i])
    for i in range (len(l)):
        newL.append(l[i])
    return newL 


def List_appendafter(l,z):
    newL=[]
    for i in range (len(l)):
        newL.append(l[i])
    for i in range (len(z)):
        newL.append(z[i])
    return newL 



def ListAvg(l):
    sum=0
    for i in range(len(l)):
        sum=sum+l[i]
    avg=sum/len(l) 
    return avg  
l=[1,2,3,4]
print(ListAvg(l))