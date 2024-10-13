# calculate the factorial of number
print("enter number")
n=int(input())

# lets num is 5
# fact=1*2*3*4*5
i=1
fact=1
while(i<=n):
    fact=fact*i
    i=i+1 
print("factorian of",n,"is",fact)
