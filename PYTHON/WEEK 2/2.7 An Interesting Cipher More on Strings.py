alpha='abcdefghijklmnopqrstuvwxyz'

i=0
print(alpha[i])
print(alpha[i+1])
print(alpha[i+2])
print(alpha[i+3])

i=15
print(alpha[i])
print(alpha[i+1])
print(alpha[i+2])
print(alpha[i+3])
print(alpha[i+4])

i=20
print(alpha[i])
print(alpha[i+1])
print(alpha[i+2])
print(alpha[i+3])
print(alpha[i+4])


i=24
print(alpha[i])
print(alpha[i+1])
# print(alpha[i+2]) OUT OF RANGE
# print(alpha[i+3]) OUT OF RANGE

i=24
print(alpha[i])
print(alpha[(i+1)%26])
print(alpha[(i+2)%26])
print(alpha[(i+3)%26])

# caesar cipher code

s='samar'
t=''
i=0
t=t+(alpha[(((alpha.index(s[i]))+1)%26)])
t=t+(alpha[(((alpha.index(s[i+1]))+1)%26)])
t=t+(alpha[(((alpha.index(s[i+2]))+1)%26)])
t=t+(alpha[(((alpha.index(s[i+3]))+1)%26)])
t=t+(alpha[(((alpha.index(s[i+4]))+1)%26)])

print(t)

s='india'
t=''
i=0
t=t+(alpha[(((alpha.index(s[i]))+1)%26)])
t=t+(alpha[(((alpha.index(s[i+1]))+1)%26)])
t=t+(alpha[(((alpha.index(s[i+2]))+1)%26)])
t=t+(alpha[(((alpha.index(s[i+3]))+1)%26)])
t=t+(alpha[(((alpha.index(s[i+4]))+1)%26)])

print(t)

s='delhi'
t=''
i=0
k=3
t=t+(alpha[(((alpha.index(s[i]))+k)%26)])
t=t+(alpha[(((alpha.index(s[i+1]))+k)%26)])
t=t+(alpha[(((alpha.index(s[i+2]))+k)%26)])
t=t+(alpha[(((alpha.index(s[i+3]))+k)%26)])
t=t+(alpha[(((alpha.index(s[i+4]))+k)%26)])

print(t)
