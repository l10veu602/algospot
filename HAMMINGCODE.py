for i in xrange(input()):
    a = map(int, '0' + raw_input())
    p = (a[1]^a[3]^a[5]^a[7]) + 2*(a[2]^a[3]^a[6]^a[7]) + 4*(a[4]^a[5]^a[6]^a[7])
    a[p] = 1 - a[p]
    a = map(str, a)
    print a[3]+a[5]+a[6]+a[7]
    
