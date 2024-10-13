num=int(input("enter number to find factorial :"))
fact=1
if(num<0):
     print("NOT DEFINE")
else:
     while(num>0):
         fact=fact*num
         num=num-1    
     print("factor of guven number is",fact)    
    
    
# to calculate no of digit

num=abs(int(input("enter number to calculate no of digit :")))
digit=1
while(num>9):
     num=num//10
     digit+=1
print("number of digit in is",digit) 

# reverse

n=int(input())
absnum=abs(n)
reversed_num=0
if(n>=0):
     while n > 0:
          # Extract the last digit
          last_digit = n % 10
          
          # Append it to the reversed number
          reversed_num = reversed_num * 10 + last_digit
          
          # Remove the last digit from the original number
          n = n // 10
     print(reversed_num)
else:
     while absnum > 0:
          # Extract the last digit
          last_digit = absnum % 10
          
          # Append it to the reversed number
          reversed_num = reversed_num * 10 + last_digit
          
          # Remove the last digit from the original number
          absnum = absnum // 10
     print(reversed_num-2*reversed_num)    


# pallindrome

n=int(input())
original_num=n
reversed_num=0

if(n<0):
    print("not pallindrome")
else:
     while n > 0:
          # Extract the last digit
          last_digit = n % 10
          
          # Append it to the reversed number
          reversed_num = reversed_num * 10 + last_digit
          
          # Remove the last digit from the original number
          n = n // 10
if(original_num==reversed_num):
     print("pallindrome")
else:
     print("not pallindrome")