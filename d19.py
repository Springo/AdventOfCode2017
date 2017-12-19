def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines

lines = readFile("d19input.txt")
nlines = []
for l in lines:
    nlines.append(list(l))
obarr = [[0] * len(nlines[0]) for _ in range(len(nlines))]

for i in range(len(nlines)):
    for j in range(len(nlines[i])):
        c = nlines[i][j]
        if c != ' ':
            if c == '|' or c == '+' or c == '-':
                obarr[i][j] = 1
            else:
                obarr[i][j] = c

x = nlines[0].index('|')
y = 0
maxx = len(nlines[0]) - 1
maxy = len(nlines) - 1
dir = 2
done = False
path = ""
steps = 0
while not done:
    steps += 1
    if obarr[y][x] != 1:
        path = path + obarr[y][x]
    if dir == 0:
        if y > 0 and obarr[y - 1][x] != 0:
            y -= 1
        else:
            if x > 0 and obarr[y][x - 1] != 0:
                dir = 3
                x -= 1
            elif x < maxx and obarr[y][x + 1] != 0:
                dir = 1
                x += 1
            else:
                done = True
    elif dir == 1:
        if x < maxx and obarr[y][x + 1] != 0:
            x += 1
        else:
            if y > 0 and obarr[y - 1][x] != 0:
                dir = 0
                y -= 1
            elif y < maxy and obarr[y + 1][x] != 0:
                dir = 2
                y += 1
            else:
                done = True
    elif dir == 2:
        if y < maxy and obarr[y + 1][x] != 0:
            y += 1
        else:
            if x > 0 and obarr[y][x - 1] != 0:
                dir = 3
                x -= 1
            elif x < maxx and obarr[y][x + 1] != 0:
                dir = 1
                x += 1
            else:
                done = True
    elif dir == 3:
        if x > 0 and obarr[y][x - 1] != 0:
            x -= 1
        else:
            if y > 0 and obarr[y - 1][x] != 0:
                dir = 0
                y -= 1
            elif y < maxy and obarr[y + 1][x] != 0:
                dir = 2
                y += 1
            else:
                done = True
print(path)
print(steps)

