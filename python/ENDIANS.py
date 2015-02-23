import struct

for i in xrange(int(raw_input())):
    print struct.unpack('<I', struct.pack('>I', int(raw_input())))[0]
