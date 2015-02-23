import re
print len(set(tuple(re.split(' ?[-._/] ?',raw_input().lower())[-3:]) for _ in xrange(input())))