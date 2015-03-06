r=lambda:map(int,raw_input().split())
def go(x,y):
    x-=1
    y-=1
    b=[0 for i in xrange(n)]
    b[x]=b[y]=1

    c=1
    while c:
        c=0
        for i in xrange(n):
            if not b[i]:
                b[i]=sum(b[j] for j in xrange(n) if t[i][j])>=2
                c=c or b[i]

    return sum(i for i in b)

for _ in xrange(input()):
    n=input()
    t=[r() for i in xrange(n)]
    print ' '.join(str(go(*r())) for i in xrange(input()))