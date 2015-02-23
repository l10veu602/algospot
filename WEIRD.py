import math

b = [False for i in xrange(500001)]

def divs(n):
    l = [1]
    for i in xrange(2, int(math.sqrt(n)) + 1):
        if n%i==0:
            l.append(i)
            if i*i!=n:
                l.append(n/i)

    return l;

def exists(l, n):
    for i in xrange(0, n+1):
        b[i] = False

    b[0] = True
    p = [0]
    for i in l:
        for j in p[:len(p)]:
            k = i+j
            if k==n:
                return True
            if k<n and b[k] == False:
                b[k] = True
                p.append(k)

    return False

for i in xrange(input()):
    n = input()
    ds = divs(n)
    print "weird" if sum(ds) > n and exists(ds, n) == False else "not weird"


