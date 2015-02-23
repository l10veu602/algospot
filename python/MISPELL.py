for i in xrange(input()):
    n,s = raw_input().split()
    n = int(n)
    print i+1, s[:n-1] + s[n:]
