def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines

lines = readFile("d08input.txt")
slines = []
for line in lines:
    splitline = line.split()
    slines.append(splitline)

regs = dict()
maxheld = dict()
for ins in slines:
    succ = False
    if ins[4] not in regs:
        regs[ins[4]] = 0
        maxheld[ins[4]] = 0
    val1 = regs[ins[4]]
    val2 = int(ins[6])
    op = ins[5]
    if op == '>':
        if val1 > val2:
            succ = True
    elif op == '<':
        if val1 < val2:
            succ = True
    elif op == '>=':
        if val1 >= val2:
            succ = True
    elif op == '<=':
        if val1 <= val2:
            succ = True
    elif op == '==':
        if val1 == val2:
            succ = True
    elif op == '!=':
        if val1 != val2:
            succ = True
    else:
        print("WHOA!")

    if succ:
        if ins[0] not in regs:
            regs[ins[0]] = 0
            maxheld[ins[0]] = 0
        if ins[1] == 'inc':
            regs[ins[0]] += int(ins[2])
            if regs[ins[0]] > maxheld[ins[0]]:
                maxheld[ins[0]] = regs[ins[0]]
        elif ins[1] == 'dec':
            regs[ins[0]] -= int(ins[2])
            if regs[ins[0]] > maxheld[ins[0]]:
                maxheld[ins[0]] = regs[ins[0]]
        else:
            print("NOOOO")

vals = []
for key in maxheld:
    vals.append(maxheld[key])
print(max(vals))

