import heapq
for c in xrange(input()):
    input()
    q = map(int, raw_input().split())
    heapq.heapify(q)
    a = 0
    while len(q)>1:
        s = heapq.heappop(q) + heapq.heappop(q)
        heapq.heappush(q,s)
        a += s

    print a
