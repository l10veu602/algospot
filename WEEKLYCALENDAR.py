wds = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
ds = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mds = [(str(m), str(d)) for m in xrange(1, 13) for d in xrange(1, ds[m]+1)]

for t in xrange(input()):
    m,d,wd = raw_input().split()
    s = mds.index((m, d)) - wds.index(wd)
    print ' '.join([mds[i%365][1] for i in xrange(s, s+7)])
