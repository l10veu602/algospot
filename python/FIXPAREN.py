p = {'(':')', '{':'}', '[':']', '<':'>'}
rp = {}
for i in p:
    rp[p[i]] = i

for t in xrange(input()):
    s = []
    bs, pr = raw_input().split()
    ans = [c for c in bs]
    for i, b in enumerate(bs):
        if b in p:
            s.append(i)
        else:
            t = s.pop()
            ob = bs[t]
            if pr.index(ob) > pr.index(rp[b]):
                ans[t] = rp[b]
            else:
                ans[i] = p[ob]
                    
    print ''.join(ans)
