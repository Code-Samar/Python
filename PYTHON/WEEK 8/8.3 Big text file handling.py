f=open('directory.txt','r')
flag=0
s='0'
while(s!=''):
    s.readline()
    if (s!=''):
        n=int(s)
        if(n==7061262898):
            print("the number found")
            flage=1
            break
        
if(flag==0):
    print("the number was not found")