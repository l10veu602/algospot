from collections import deque

h = 0
w = 0
m = []
es = []
cm = {}
vs = []

def addEdge(t, f):
    es[f].append(t)
    es[t].append(f)

def makeEdges():
    for i in xrange(h):
        for j in xrange(w):
            f = i*w + j
            for k in xrange(i+1, h):
                t = k*w + j
                addEdge(f, t)
                if m[k][j] != '.':
                    break
                
            for k in xrange(j+1, w):
                t = i*w + k
                addEdge(f, t)
                if m[i][k] != '.':
                    break

def pathCount(p):
    c = m[p/w][p%w]
    if c == '.' or len(cm[c]) == 1:
        return 0
    
    d = deque()
    for i in xrange(h*w):
        vs[i] = -1

    vs[p] = 0
    d.append((p, 0))
    while len(d) > 0 and d[0][1] < 4:
        t, l = d.popleft()
        vs[t] = l
        if l != 0 and m[t/w][t%w] != '.':
            continue
        nl = l+1
        for v in es[t]:
            if vs[v] == -1:
                vs[v] = nl
                d.append((v, nl))

    count = 0;
    for i in cm[c]:
        if vs[i]>0 and vs[i]<4:
            count += 1
    return count

for t in xrange(input()):
    h,w = map(int, raw_input().split())
    m = [raw_input() for i in xrange(h)]
    cm = {}
    for i in xrange(h):
        for j in xrange(w):
            c = m[i][j]
            if c == '.':
                continue
            if c not in cm:
                cm[c] = []
            cm[c].append(i*w+j)
                
    es = [[] for i in xrange(h*w)]
    makeEdges()
    
    vs = [-1]*h*w
    ans = 0
    for y in xrange(h):
        for x in xrange(w):
           ans += pathCount(y*w+x)
    print ans/2
