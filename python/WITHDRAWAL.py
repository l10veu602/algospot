rs=lambda:map(int,raw_input().split())
for _ in xrange(input()):
    n,k=rs()
    rc=rs()
    l,h=0.0,1.0
    while h-l>1e-8:
        m=(h+l)/2
        v=sorted(map(lambda a:m*a[1]-a[0],zip(*[iter(rc)]*2)))
        h,l=(m,l) if sum(v[n-k:])>=0 else (h,m)

    print "%.10f"%(h)