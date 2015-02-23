import sys
r = lambda: map(int, raw_input().split())
for _ in xrange(input()):
    input()
    m,e = r(),r()
    t = reversed(sorted(zip(e,m)))
    a,c = 0,0
    for x,y in t:
        c += y
        a = max(a, c+x)

    print a
