st={1,2,3,4,1,5,3,7,1,2,4,3,5}
print(st) #no duplicate element

# print(st[0]) #error

# all mathemetical operation of set cam be implimente

a={1,3,5}
b={1,2,3,4,5,6}
print(a)
print(b)
print(a.issubset(b))
print(a.issuperset(b))

# union
a={1,3,5}
b={1,2,4,6}
c1=a.union(b)
c2=a|b
print(c1,c2)

# intersection 
a={1,3,5}
b={1,2,4,6}
c1=a.intersection(b)
c2=a&b
print(c1,c2)

#difference
a={1,3,5}
b={1,2,4,6}
c1=a.difference(b)
c2=a-b
print(c1,c2)
