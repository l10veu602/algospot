c = { "kg": [2.2046, "lb"], "lb": [0.4536, "kg"], "l": [0.2642, "g"], "g": [3.7854, "l"] }
for i in xrange(input()):
    a,b = raw_input().split()
    p = c[b]
    print i+1, "%.4f"%(float(a)*p[0]), p[1]
