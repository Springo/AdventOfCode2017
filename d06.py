def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line)
    return lines

lines = readFile("d06input.txt")
splitline = lines[0].split()
intlines = [int(val) for val in splitline]

seen = dict()
seen[str(intlines)] = 0
done = False
iters = 0
while not done:
    maxind = 0
    iters += 1
    for i in range(len(intlines)):
        if intlines[i] > intlines[maxind]:
            maxind = i
    nums = intlines[maxind]
    intlines[maxind] = 0
    for i in range(1, nums + 1):
        intlines[(maxind + i) % len(intlines)] += 1
    if str(intlines) in seen:
        done = True
        print(iters - seen[str(intlines)])
    else:
        seen[str(intlines)] = iters
print(iters)