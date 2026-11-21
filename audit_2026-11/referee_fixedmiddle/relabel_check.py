import rule
def Rn(n):
    p={}
    if n%2:
        k=(n-1)//2; p[0]=(n,n+1); p[1]=(0,2*n-1); p[2]=(n-1,n-2)
        for j in range(1,k): p[n+1-2*j]=(2*j,2*j-1); p[n-2*j]=(2*n-1-2*j,2*n-2*j)
    else:
        k=(n-2)//2; p[0]=(n-2,n-1); p[1]=(1,2*n-1); p[2]=(0,2*n-2); p[3]=(n+1,n)
        for j in range(1,k): p[n+1-2*j]=(2*j+1,2*j); p[n-2*j]=(2*n-2-2*j,2*n-1-2*j)
    return p
r=lambda i: 0 if i==0 else i+1
for n in range(3,30):
    a=rule.pairs(n); b={q:(r(P),r(M)) for q,(P,M) in Rn(n).items()}
    assert a==b,(n,a,b)
print("relabeling of R_n matches explicit M_n lists for n=3..29")
