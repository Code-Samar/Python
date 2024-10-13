def obvious_sort(l):
    
    x=[]
    while(len(l)>0):
        mini=l[0]
        for i in range(len(l)):
            if l[i]<mini:
                mini=l[i]
        x.append(mini)
        l.remove(mini)
    return x
l=[90,23,6,75,96,26]        
print(obvious_sort(l))