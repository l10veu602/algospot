l = ['zero','one','two','three','four','five','six','seven','eight','nine','ten']
for i in xrange(input()):
    a,o,b,e,c = raw_input().split()
    ans = eval('l.index(a)'+o+'l.index(b)')
    print "No" if ans<0 or ans>10 or set(l[ans]) != set(c) else "Yes"
