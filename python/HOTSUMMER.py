for i in xrange(input()):
    t = input()
    s = sum(map(int, raw_input().split()))
    print "YES" if int(s)<=t else "NO"
