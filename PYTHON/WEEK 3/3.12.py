''' 
employ_id=int(input("enter trade id :"))
while(employ_id != -1):
    trade=int(input("enter trade amount :"))
    profit_loss=0
    while(trade!=0):
        profit_loss=profit_loss+trade
        trade=int(input("enter trade amount :"))   
    print(f'profit/loss for {employ_id} is {profit_loss}')  
    employ_id=int(input("enter trade id :"))  
'''
'''
no_days=int(input("enter no of days"))
for i in range(1,no_days+1):
    rainfall=int(input("enter the rainfall"))
    total_rainfall=0
    while(rainfall!=-1):
        total_rainfall=total_rainfall+rainfall
        rainfall=int(input("enter the rainfall"))
    print(f'total rainfall for day {i} is {total_rainfall}')
''' 

word=input("enter word :")
maxLen=0
while(word!='-1'):
    count=0
    for latter in word:
        count=count+1
    if(count>maxLen):
        maxLen=count   
    word=input("enter word :")    
    
print("the lenght of longest word is %s:" %maxLen)    