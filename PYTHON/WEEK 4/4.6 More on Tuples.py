t=1,2,3
print(t, type(t))

x,y,z=t
print(x,y,z)

l=[10]
print(l,type(l))

t=(10) #int
print(t,type(t))

t=(10,) #upple
print(t,type(t))

# list inside tupple

t=([1,2],['a','b']) #non hashable , value inside tupple is mutable
#t[0]=10 # we can't insert element in tupple
t[0][0]=10 # we can insert element in list
print(t,type(t))