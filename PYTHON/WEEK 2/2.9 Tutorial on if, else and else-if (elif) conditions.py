# odd/even number

num=int(input("enter the number"))
if (num % 2 == 0):
    print("enven number")
else:
    print("odd number")    
    

# find wethwe number ends with 0 5 or other

num=int(input("enter the number :"))
if(num%5==0):
    if(num%10==0):
        print("END WITH 0")
    else:
        print("END WITH 5")
else:
    print("other")            
    
# print grade for 0-100 marks

# if else
marks=int(input("enter marks")) 
if (marks<=100 and marks>=0):
    if(marks>=90):
        print("A")
    if(marks>=80 and marks<90):
        print("B")    
    if(marks>=70 and marks<80):
        print("C")
    if(marks>=60 and marks<70):
        print("D") 
    if(marks<60):
        print("E")    
else:
    print("INVALID MARKS")               
    
    
    
#  elif   
marks=int(input("enter marks")) 
if (marks<=100 and marks>=0):
    if(marks>=90):
        print("A")
    elif(marks>=80):
        print("B")    
    elif(marks>=70):
        print("C")
    elif(marks>=60):
        print("D") 
    else:
        print("E")    
else:
    print("INVALID MARKS")             
   
    
