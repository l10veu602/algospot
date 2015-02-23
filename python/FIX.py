for _ in xrange(input()):
    input()
    print sum(a==b for a,b in enumerate(map(int,raw_input().split()),1))