import math
print(math.log(10))
print(math.sqrt(16))
print(math.sin(90))
print(math.factorial(5))
print(math.pow(10,3))

# let us simulate a coin toss
import random

a=random.random()
if(a >= 0.5 ):
    print("HEADS")
else:
    print("TAIL")    

print(random.random())


# let us simulate a DICE (6 FACE)
import random
# print(random.randrange(1,7)

dice1=(random.randrange(1,7))
dice2=(random.randrange(1,7))
total = dice1+dice2
print("your pair of dice is : ",total)