jumps = [102,255,99,252,200,24,219,57,103,2,226,254,1,0,69,216]
seq = [i for i in range(256)]
skip = 0
pos = 0

rawinp = "102,255,99,252,200,24,219,57,103,2,226,254,1,0,69,216"
ascvals = [ord(c) for c in rawinp]
ascvals.extend([17, 31, 73, 47, 23])

def swapnums(start, swappers):
    for i in range(len(swappers)):
        seq[(i + start) % 256] = swappers[i]

for _ in range(64):
    for j in ascvals:
        if j < 256:
            if pos + j >= 256:
                swappers = seq[pos:]
                remaining = j - (256 - pos)
                swappers.extend(seq[:remaining])
                rev = swappers[::-1]
                swapnums(pos, rev)
            else:
                swappers = seq[pos:pos + j]
                rev = swappers[::-1]
                swapnums(pos, rev)
            pos = (pos + skip + j) % 256
        skip += 1

dense = []
for i in range(16):
    xorval = seq[16 * i]
    for j in range(1, 16):
        xorval = xorval ^ seq[16 * i + j]
    dense.append(xorval)

hexnums = []
for d in dense:
    hexnums.append((hex(d))[2:])

finalhash = ""
for h in hexnums:
    if len(h) == 2:
        finalhash += h
    else:
        finalhash += "0" + h

print(finalhash)

print(seq[0] * seq[1])