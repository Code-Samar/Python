l1=[1,2,3]
l2=[10,20,30]
l3=[100,200,300]

# add in sequence
l12=l1+l2
l21=l2+l1

l123=l1+l2+l3

print(l12,l21,l123)
print(l12)
print(l21)
print(l123)


l1=[0,0,0,0,0,0,0,0,0,0]
print(l1)

l2=[0]*10 #[0,0,0,0,0,0,0,0,0,0]
print(l2)

l1=[1,2,3]
l2=[1,2,3]
l3=[1,3,2]
print(l1==l2) # true
print(l1==l3) # false bcz sequence of element element also consider

print(l1<l2)

# mutability
# LIST IS MUTABLE
# sring is immutable
l=[1,2,3]
print(l)
l[2]=3
print(l)


x=5 # stored on adress
y=x # stored on adress
x=10# replace from stored on adress
print(x,y) # 10 5

l1=[1,2,3]
l2=l1
l1[0]=100
print(l1,l2) # [100,2,3] [100,2,3] not not same as integer bcz internal implimentation



l1=[1,2,3]
l2=list(l1)
l3=l1[:]
l4=l1.copy()
l5=l1

l2[0]=100
l3[1]=200
l4[2]=300

print(l1,l2,l3,l4)

print(l1 is l2)
print(l1 is l3)
print(l1 is l4)
print(l1 is l5)


l=[1,2,3]
print(l)

l.append(4) # at end
print(l)

l.insert(2,9) # at index
print(l)

l.remove(2) #delete the element 2
print(l)

l.pop(0) # deleted element at index like 0
print(l)

l1=[1,2,6,3,8,6,4,2,9]
l1.sort()
print(l1)

s=[1,2,3,4,5,6,7,8,9]
s.reverse()
print(s)