def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines

lines = readFile("d12input.txt")
adjlist = dict()
for line in lines:
    splitline = line.split(' <-> ')
    dest = splitline[1].split(', ')
    destint = [int(a) for a in dest]
    adjlist[int(splitline[0])] = destint

counter = 0
found = dict()
for key in adjlist:
    if key not in found:
        counter += 1
        q = [key]
        while len(q) > 0:
            a = q.pop(0)
            if a not in found:
                found[a] = 1
                for elem in adjlist[a]:
                    q.append(elem)

print(counter)