# functional programming apraoch

a=10
b=20

if a<b:
    small=a
else:
    small=b
print('small is ',small)    

small=a if a<b else b # inline
print(small)

a=5
while a>0:
    print(a)
    a=a-1
    
a=6   
while a>0:print(a);a=a-1    

fruits={'mango','banana','apple','orange','pineapple','watermelon','guava','kiwi'}
newList=[]
for fruit in fruits:
    if 'n' in fruit:
        newList.append(fruit.capitalize())
print(newList) 

        
newList=[fruit.capitalize() for fruit in fruits if 'n' in fruit]  
print(newList)    
