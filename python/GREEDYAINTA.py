import gc
for _ in xrange(input()):
    gc.collect()
    input()
    a=map(int,raw_input().split())
    c,p=0,1
    for i in xrange(len(a)-1,0,-1):
        if (a[i]+c)%i:
            p=0
            break
        c+=(a[i]+c)/i

    print ("" if p else "IM") + "POSSIBLE"