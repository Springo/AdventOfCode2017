def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines

lines = readFile("d13input.txt")
layers = []
for line in lines:
    arr = line.split(': ')
    layers.append([int(a) for a in arr])

ldic = dict()
maxl = 0
for l in layers:
    ldic[l[0]] = l[1]
    maxl = l[0]

delay = 0
sev = 1300
while sev > 0:
    sev = 0
    for i in range(maxl + 1):
        if i in ldic:
            pathlen = ldic[i] * 2 - 2
            if (i + delay) % pathlen == 0:
                sev += 1
    delay += 1
print(delay - 1)
