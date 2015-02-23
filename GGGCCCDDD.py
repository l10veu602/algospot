R=1000000007
def exp(n,m):
    r=1
    if m>0:
        h=exp(n,m/2)
        r=h*h%R
        if m%2:
            r=r*n%R

    return int(r)

for _ in xrange(input()):
    n,m=map(int,raw_input().split())
    c=[0]*(n+1)
    s=0
    for i in xrange(n,0,-1):
        c[i]=exp(n/i,m)
        for j in xrange(i+i,n+1,i):
            c[i]-=c[j]
            if c[i]<0:
                c[i]+=R

        s+=c[i]*i
        s%=R

    print s