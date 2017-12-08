def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines

def getWeight(key):
    if key not in adjlist:
        return weights[key]
    total = weights[key]
    for adj in adjlist[key]:
        total += getWeight(adj)
    return total

def isBalanced(key):
    if key not in adjlist:
        return True
    res = getWeight(adjlist[key][0])
    for adj in adjlist[key]:
        if res != getWeight(adj):
            return False
    return True

lines = readFile("d07input.txt")
bases = dict()
adjlist = dict()
weights = dict()
print(len(lines))
for line in lines:
    if '->' in line:
        splitline = line.split(' -> ')
        super = splitline[0].split()
        supertow = super[0]
        weight = int(super[1][1:-1])
        subtow = splitline[1].split(', ')
        weights[supertow] = weight
        if supertow not in bases:
            bases[supertow] = 1
        adjlist[supertow] = []
        for sub in subtow:
            adjlist[supertow].append(sub)
            bases[sub] = 0
    else:
        super = line.split()
        supertow = super[0]
        weight = int(super[1][1:-1])
        weights[supertow] = weight

print(len(weights))
for key in adjlist:
    #if bases[key] == 1:
    #    print(key)
    if not isBalanced(key):
        print(key)

print(adjlist['bvrxeo'])
for stuff in adjlist['bvrxeo']:
    print(getWeight(stuff))
print(weights['ltleg'])
