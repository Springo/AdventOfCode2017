rawinp = "wenycdww"
#rawinp = "flqrgnkx"
seq = [i for i in range(256)]

def swapnums(start, swappers):
    for i in range(len(swappers)):
        seq[(i + start) % 256] = swappers[i]

def gethash(rawinp):
    global seq
    seq = [i for i in range(256)]
    skip = 0
    pos = 0
    ascvals = [ord(c) for c in rawinp]
    ascvals.extend([17, 31, 73, 47, 23])
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
    return finalhash

def converthash(hash):
    finalhash = ""
    for c in hash:
        finalhash += bin(int(c, 16))[2:].zfill(4)
    return finalhash

total = 0
board = []
for i in range(128):
    inp = rawinp + "-" + str(i)
    h = gethash(inp)
    conv = converthash(h)
    total += conv.count('1')
    board.append(conv)

counter = 1
gboard = [[0] * 128 for _ in range(128)]
merges = dict()
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == '1':
            if i > 0 and board[i - 1][j] == '1':
                gboard[i][j] = gboard[i - 1][j]
                if j > 0 and board[i][j - 1] == '1' and gboard[i][j] != gboard[i][j - 1]:
                    a = gboard[i][j]
                    b = gboard[i][j - 1]
                    done = False
                    key1 = -1
                    key2 = -1
                    for key in merges:
                        if a in merges[key]:
                            key1 = key
                        if b in merges[key]:
                            key2 = key
                    if key1 == -1 and key2 == -1:
                        merges[a] = [a, b]
                    elif key1 == -1:
                        merges[key2].append(a)
                    elif key2 == -1:
                        merges[key1].append(b)
                    elif key1 == key2:
                        done = True
                    else:
                        merges[key1].extend(merges[key2])
                        merges[key2] = []

            elif j > 0 and board[i][j - 1] == '1':
                gboard[i][j] = gboard[i][j - 1]
            else:
                gboard[i][j] = counter
                counter += 1

dups = 0
for key in merges:
    if len(merges[key]) > 0:
        dups += len(merges[key]) - 1


print(total)
print(counter - 1 - dups)