def calc(m,n):
    return m*100/n

for t in xrange(input()):
    n,m = map(int, raw_input().split())
    z = calc(m,n)
    lb,ub = 0, 2147483647
    while lb+1<ub:
        mid = (lb+ub)/2
        if calc(m+mid,n+mid)>z:
            ub = mid
        else:
            lb = mid

    print ub if calc(m+ub,n+ub)>z else -1
