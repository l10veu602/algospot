rl=lambda:map(int,raw_input().split())
for _ in xrange(input()):
    r,c=rl()
    m=[[0 for j in xrange(c+2)] for i in xrange(r+2)]
    for i in xrange(r):
        m[i+1][1:c+1]=rl()
    for i,y in enumerate(m[1:r+1],1):
        l=[]
        for j,x in enumerate(y[1:c+1],1):
            A,B,C=y[j-1],m[i-1][j],m[i-1][j-1]
            f=map(lambda z:x-z,[0,A,B,(A+B)/2,A+B-C])
            af=map(lambda z:abs(z),f)
            mi=af.index(min(af))
            l+=[mi,f[mi]]
        print ' '.join(map(str,l))