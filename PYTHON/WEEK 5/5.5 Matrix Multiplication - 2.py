
r1=[1,2,3]
r2=[4,5,6]
r3=[7,8,9]
    
s1=[4,6,7]
s2=[6,7,3]
s3=[5,2,7]

a=[]
b=[]
a.append(r1)
a.append(r2)
a.append(r3)

b.append(s1)
b.append(s2)
b.append(s3)

dim=3
c=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(dim):
    for j in range(dim):
        for k in range(dim):
            c[i][j]=c[i][j]+a[i][k]*b[k][j]

print(c)

