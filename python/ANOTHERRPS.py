while 1:
    a,n=0,input()-1
    if n<0:
        break
    while n:
        a,n=(a+n)%3,n/3
    print 'PSR'[a]