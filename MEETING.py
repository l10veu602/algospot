rl = lambda: sorted(map(int, raw_input().split()))
for t in xrange(input()):
    input()
    print sum(abs(a-b) for a,b in zip(rl(),rl()))
