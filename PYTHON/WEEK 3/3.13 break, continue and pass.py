'''  

email=input("enter your email id :")
for i in email:
    if(i=='@'):
        break
    print(i, end='')

'''   
email=input("enter your email id :")
for i in email:
    if(i=='@'):
        print('')
        continue
    print(i,end='')    
    
    
for x in range(11):
    if(x%3==0):
        print(x)
    else:
        pass
       