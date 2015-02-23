M=10000001
c=[2]*M
c[0]=c[1]=1
for i in xrange(2,3163):
    ii=i*i
    for j in xrange(ii,M,i):
        c[j]+=2 if ii<j else 1

for _ in xrange(input()):
    n,l,h=map(int,raw_input().split())
    a=0
    for i in xrange(l,h+1):
        if c[i]==n:
            a+=1

    print a
