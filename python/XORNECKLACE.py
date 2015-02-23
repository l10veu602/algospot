for _ in xrange(input()):
    input()
    a=map(int,raw_input().split())
    print sum(x^y for x,y in zip(a,a[1:]+a[0:1]))