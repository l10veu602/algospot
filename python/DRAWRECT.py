for i in xrange(int(raw_input())):
    x = 0
    y = 0
    for j in xrange(3):
        s = raw_input().split();
        x ^= int(s[0])
        y ^= int(s[1])

    print x, y
