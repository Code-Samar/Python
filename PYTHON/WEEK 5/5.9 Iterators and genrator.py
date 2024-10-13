#fruits=['mango','apple','banana','orange','guava','kiwi',
#        'pineapple','watermwlon']
#for fruit in fruits:
#    print(fruit)
    
#basket=iter(fruits)    

#print(basket)

# print(next(basket))
# print(next(basket))
# print(next(basket))

def square(limit):
    x=0
    while x < limit:
        yield x * x
        yield x * x * x
        x +=1
        
a=square(5)   
print(next(a),next(a)) 
print(next(a),next(a))     
print(next(a),next(a)) 
print(next(a),next(a)) 
print(next(a),next(a)) 
