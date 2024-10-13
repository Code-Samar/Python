def initialize_mat(dim):
    c=[]
    for i in range(dim):
        c.append([])
    for i in range(dim):
        for j in range (dim):
            c[i].append(0)    
    return c


def dot_product(u,v):
    dim=len(u)    
    ans=0  
    for i in range(dim):
        ans= ans+(u[i]*v[i])  
    return ans

def row(m,i):
    dim=len(m)
    l=[]
    for k in range(dim):
        l.append(m[i][k])
    return l    

def column(m,j):
    dim=len(m)
    l=[]
    for k in range(dim):
        l.append(m[k][j])
    return l    

def mat_mul(a,b):
    dim=len(a)
    c=initialize_mat(dim)
    for i in range(dim):
        for j in range(dim):
            c[i][j]=dot_product(row(a,i),column(b,j))
    return c



