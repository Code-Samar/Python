# boolian data type
b1=True
b2=False
print(type(b1))
print(type(b2))

# type casting

# 1 int type from another
x=int(51)
y=int(26.7)
# z=int('samar') #not possible its syntax error
w=int(False) 
print(x,type(x)) # 51 int type
print(y,type(y)) # 26 int type
# print(type(z))
print(w,type(w)) # 0 for false and 1 for true int type 

# float type from another
a=float(5)
b=float(2.6)
# c=float('samar') #syntax error
d=float(True)
e=float(False)
# f=float('') #syntax error

print(a,type(a)) 
print(b,type(b)) 
print(d,type(d))
print(e,type(e))

#boolean type from another
p=bool('10')
q=bool('sam')
r=bool('') 
s=bool(2)
print(p,type(p)) 
print(q,type(q)) 
print(r,type(r))
print(s,type(s))