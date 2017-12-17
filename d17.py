from blist import *

step = 369
pos = 0

buff = blist([0])
for i in range(1, 50000001):
    pos = (pos + step) % len(buff)
    buff.insert(pos + 1, i)
    pos += 1
    if i % 1000000 == 0:
        print(i)
print(buff[pos + 1])
print(buff[buff.index(0) + 1])