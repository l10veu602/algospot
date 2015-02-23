def go(i):
    if len(e[i])==0:
        s[i]=3
        return

    s[i]=1
    f=0
    for j in e[i]:
        if s[j]==0:
            go(j)
            if s[j]==2:
                f=1

    s[i]=3 if f==1 else 2

e=[[] for i in xrange(1000)]
rp=lambda:map(int,raw_input().split())
for _ in xrange(input()):
    g,h=rp()
    for i in xrange(g):
        e[i][:]=[]

    for i in xrange(h):
        a,b=rp()
        e[a].append(b)
        e[b].append(a)

    s=[0]*g
    for i in xrange(g):
        if s[i]==0:
            go(i)

    print len(filter(lambda x:x==3,s))
