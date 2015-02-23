def go(n,c):
    if n==0:
        return 10000
    elif m[n][c] != -1:
        return m[n][c]

    a,cc=0,0
    nc=c
    for i in cs[n-1]:
        if nc==0:
            break

        cc+=i
        nc-=1
        a=max(a,min(cc/rs[n-1],go(n-1, nc)))

    m[n][c]=a
    return a

r=lambda:map(int,raw_input().split())
for _ in xrange(input()):
    n=input()
    rs,cs=[],[]
    for i in xrange(n):
        rs.append(r()[0])
        cs.append(sorted(r(), reverse=1))

    c=min(10,sum(len(c) for c in cs))
    m=[[-1 for i in xrange(c+1)] for i in xrange(n+1)]
    print go(n,c)