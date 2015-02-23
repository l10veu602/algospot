def partial(s):
    m = len(s)
    pi = [0]*m
    begin = 1
    matched = 0
    while begin+matched < m:
        if s[begin+matched] == s[matched]:
            matched += 1
            pi[begin+matched-1] = matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched-1]
                matched = pi[matched-1]
    return pi

for t in xrange(input()):
    s = raw_input()
    ol = len(s)
    s = s[::-1] + s
    pt = partial(s)
    l = len(s)
    k = l-1
    while pt[k] > ol:
        k = pt[k]-1

    print l - pt[k]
