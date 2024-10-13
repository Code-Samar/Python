s='VIBGYOR'
for i in range (7) :
    print(s[i])
    
s='VIBGYOR'
for i in s:
    print(i)    

# s='VIBGYOR'
# for i in s:
#     print(s[i])  # string indices must be integers, not 'str

s='VIBGYOR'
t='VIBGYOR'
count=0
for i in range(7):
    for j in range(7):
        print(i,s[i],j,t[j])
        count=count+1
print("total number of way :",count)   
      