p = {'(':')', '{':'}', '[':']'}

for t in xrange(input()):
    s = []
    f = True
    for b in raw_input():
        if b in p:
            s.append(b)
        elif len(s) == 0 or b != p[s[-1]]:
            f = False
            break
        else:
            s.pop()

    print 'YES' if f and len(s) == 0 else 'NO'
