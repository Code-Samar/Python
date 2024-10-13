a1=[1,2,3]
a2=[4,5,6]
a3=[7,8,9]

b1=[1,2,1]
b2=[6,2,3]
b3=[4,2,1]

A=[]
A.append(a1)
A.append(a2)
A.append(a3)

B=[]
B.append(b1)
B.append(b2)
B.append(b3)

print(A)
print(B)


import numpy
x=numpy.mat(A)
y=numpy.mat(B)

print(x*y)