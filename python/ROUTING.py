import heapq

et = [[] for i in xrange(10000)]
ew = [[] for i in xrange(10000)]
hq = []
d = [-1]*10000
v = [0]*10000

for t in xrange(input()):
    n,m = map(int, raw_input().split())
    for i in xrange(n):
        et[i][:] = []
        ew[i][:] = []
    
    hq[:] = []

    for i in xrange(n):
        d[i] = -1
        v[i] = 0
    
    for i in xrange(m):
        a,b,c = raw_input().split()
        a,b,c = int(a), int(b), float(c)

        et[a].append(b)
        ew[a].append(c)

        et[b].append(a)
        ew[b].append(c)

    d[0] = 1
    heapq.heappush(hq, (d[0], 0))
    while (len(hq)>0):
        td,top = heapq.heappop(hq)
        if top == n-1:
            break;

        if v[top] == 1:
            continue

        v[top] = 1
        for ei in xrange(len(et[top])):
            to,w = et[top][ei],ew[top][ei]
            nd = td * w
            if d[to]<0 or d[to]>nd:
                d[to] = nd
                heapq.heappush(hq, (d[to], to))

    print "%.10f"%(d[n-1])
