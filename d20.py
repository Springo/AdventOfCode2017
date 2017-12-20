def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines

lines = readFile("d20input.txt")
strlines = []
for line in lines:
    splitline = line.split('>,')
    strlines.append(splitline)

def disttozero(ind):
    return abs(pss[ind][0]) + abs(pss[ind][1]) + abs(pss[ind][2])
def accdist(ind):
    return abs(pss[ind][0]) + abs(pss[ind][1]) + abs(pss[ind][2])

pss = []
vss = []
ass = []

for line in strlines:
    p = line[0][line[0].index('<') + 1:].split(',')
    pss.append([int(x) for x in p])
    v = line[1][line[1].index('<') + 1:].split(',')
    vss.append([int(x) for x in v])
    a = line[2][line[2].index('<') + 1:-1].split(',')
    ass.append([int(x) for x in a])

dead = dict()
pos = dict()
for j in range(len(pss)):
    dead[j] = False
    pos[str(pss[j])] = j

for i in range(1000):
    for j in range(len(pss)):
        if not dead[j]:
            pos[str(pss[j])] = -1
            vss[j][0] += ass[j][0]
            vss[j][1] += ass[j][1]
            vss[j][2] += ass[j][2]
            pss[j][0] += vss[j][0]
            pss[j][1] += vss[j][1]
            pss[j][2] += vss[j][2]
            if str(pss[j]) not in pos or pos[str(pss[j])] == -1:
                pos[str(pss[j])] = j
            else:
                dead[j] = True
                dead[pos[str(pss[j])]] = True
                pos[str(pss[j])] = 0

minind = 0
mindist = disttozero(0)
for j in range(len(pss)):
    if disttozero(j) < mindist:
        mindist = disttozero(j)
        minind = j
print(minind)

counter = 0
for c in dead:
    if dead[c] == False:
        counter += 1
print(counter)