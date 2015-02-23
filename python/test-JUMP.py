for t in xrange(1,5):
    l = [(0,0)]
    for i in xrange(1,t+1):
        nl = []
        for x,y in l:
            nl.append((x-i,y))
            nl.append((x+i,y))
            nl.append((x,y-i))
            nl.append((x,y+i))

        l = nl

    s = set(nl)
    print len(nl), len(s)
    print sorted(s)
