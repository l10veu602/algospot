for i in xrange(int(input())):
    s = str(raw_input())
    print ''.join(sorted([s[j:j+2] for j in xrange(0, len(s), 2)]))
