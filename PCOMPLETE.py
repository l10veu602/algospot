Q='?'
for _ in xrange(input()):
    n,s=input(),raw_input()
    p,q=map(int,raw_input().split())
    m=min(p,q)
    d={'a?':p,'b?':q,'?a':p,'?b':q,'??':2*m}
    a=m if n%2 and s[n/2]=='?' else 0
    for x,y in zip(s[:n/2],s[:n/2-1:-1]):
        a+=d[x+y] if x+y in d else 0

    print a
