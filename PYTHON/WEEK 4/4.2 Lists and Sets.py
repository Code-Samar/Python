l=list(range(10))
print(l)
print(l[1])

print(5 in l)
print(10 in l)

l='samar'
print(l[1])
print('s' in l)
print('samar' in l)
print('5' in l)

l=list(range(100000))
#print(l)
print('samar' in l)

x=[1,2,3,4,5,61,5,3,7,9]
print(type(x), x)

y={1,2,3,4,5,61,5,3,7,9}
print(type(y), y)
print(10 in y)


l=list(range(10000000))
print(-1 in l)
s=set(range(100000000))
print(-1 in s) 

z={'samar','ahmad','sahil','shamim'}
print(z)
print('laloo' in z)
z.add('laloo')
print(z)