def add(a,b,c):
    ans=a+b-c
    return ans    

print(add(10,20,5)) # positional argu
print(add(a=20, b=60, c=40))

def add(a,b=10,c=30): # default  argu
    ans=a+b-c
    return ans 

print(add(10,))   
print(add(10,20))
print(add(10,20,5))
