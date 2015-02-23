from heapq import *
r=lambda:map(int,raw_input().split())
for _ in xrange(input()):
    n,m=r()
    a=map(lambda x:-x,r())
    heapify(a)
    p=0
    for _ in xrange(m):
        t=heappop(a)
        if t==0:
            break
        p-=t
        heappush(a,t+1)

    print p
