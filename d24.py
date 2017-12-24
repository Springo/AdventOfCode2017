def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines

lines = readFile("d24input.txt")

vals = []
for line in lines:
    vals.append(sorted([int(n) for n in line.split('/')]))

adjlist = dict()
nodevals = dict()
forcedadj = dict()

counter = 0
for v in vals:
    a = v[0]
    b = v[1]
    nodevals[counter] = a
    nodevals[counter + 1] = b
    forcedadj[counter] = [counter + 1]
    forcedadj[counter + 1] = [counter]
    adjlist[counter] = []
    adjlist[counter + 1] = []
    counter += 2

for key in nodevals:
    for key2 in nodevals:
        if key != key2 and nodevals[key2] == nodevals[key]:
            adjlist[key].append(key2)

def Path(u):
    global path
    global pathl
    global bestpath
    global bestpathl
    u2 = forcedadj[u][0]
    used[u] = 1
    used[u2] = 1
    for v in adjlist[u2]:
        if v not in used or used[v] == 0:
            v2 = forcedadj[v][0]
#            path += nodevals[v] + nodevals[v2]
            path += 1
            pathl.extend([v, v2])
            if path > bestpath:
                bestpath = path
                bestpathl = pathl[:]
            elif path == bestpath:
                pipe1 = [nodevals[key] for key in bestpathl]
                pipe2 = [nodevals[key] for key in pathl]
                if sum(pipe2) > sum(pipe1):
                    bestpathl = pathl[:]
            Path(v)
#            path -= nodevals[v] + nodevals[v2]
            path -= 1
            pathl.pop()
            pathl.pop()
    used[u] = 0
    used[u2] = 0


used = dict()
path = 0
pathl = []
bestpath = 0
bestpathl = []
for key in nodevals:
    if nodevals[key] == 0:
#        path = nodevals[forcedadj[key][0]]
        path = 1
        pathl = [key, forcedadj[key][0]]
        if path > bestpath:
            bestpath = path
            bestpathl = pathl
        Path(key)

print(bestpath)
print(bestpathl)
pipe = [nodevals[key] for key in bestpathl]
print(pipe)
print(sum(pipe))