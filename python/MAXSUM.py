import gc
for t in xrange(input()):
    gc.collect()
    n = input()
    m,prev = 0,0
    for t in raw_input().split():
        t = int(t)
        prev = t if prev<0 else t+prev
        if prev>m:
            m = prev
            
    print m
