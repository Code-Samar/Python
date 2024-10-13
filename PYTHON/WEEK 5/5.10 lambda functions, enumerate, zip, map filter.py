# def add(x,y):
#     return x+y


# def sub(x,y):
#     return x-y


# def mul(x,y):
#         return x*y
    
# def div(x,y):      
#     return x/y


#lambda
add = lambda x,y : x+y
sub = lambda x,y : x-y
mul = lambda x,y : x*y
div = lambda x,y : x/y
    
    
print(add(10,20))
print(sub(10,20))
print(mul(10,20))
print(div(10,20))



fruits=['mango','apple','banana','orange','guava','kiwi',
       'pineapple','watermwlon']

size=[5,5,6,6,9,10,5,4]

for i in range(len(fruits)):
       print(i,fruits[i])

#enumerate      
for fruit in enumerate(fruits) :
       print(fruit)
 
 
#zip       
print(dict(zip(fruits,size)))
print(list(zip(fruits,size)))


#map

a=[10,20,30,40,50,60]
b=[5,10,15,20,25,30]

def sub(x,y):
    return x-y

def incr(x):
    return x+1

c=map(sub,a,b)
print(list(c))
c=map(incr,a)
print(list(c))

import math

a=[25,-16,9,81,-100]
def sq_rt(n):
    return math.sqrt(n)

def is_positive(n):
    if n>=0:
        return n
    
c=map(sq_rt,filter(is_positive,a))
print(list(c))