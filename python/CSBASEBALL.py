for _ in xrange(input()):
    a,b=map(int,raw_input().split())
    print 0 if a>b else b-a+4
