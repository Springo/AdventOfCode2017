def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines

lines = readFile("d18input.txt")
strlines = []
for line in lines:
    splitline = line.split()
    strlines.append(splitline)

regs = dict()
regs2 = dict()
regs['p'] = 0
regs2['p'] = 1
q1 = []
q2 = []

def getVal(n, dic):
    if ord(n[0]) < 58:
        return int(n)
    else:
        if n not in dic:
            dic[n] = 0
        return dic[n]


last_rec_1 = 0
last_rec_2 = 0
counter = 0
i = 0
j = 0
hold1 = False
hold2 = False
steppers = 0
while i < len(strlines) and j < len(strlines):
    l = strlines[i]
    l2 = strlines[j]
    ins = l[0]
    ins2 = l2[0]
    if ins == "snd":
        q1.append(getVal(l[1], regs))
    if ins == "set":
        arg1 = l[1]
        arg2 = l[2]
        if arg1 not in regs:
            regs[arg1] = 0
        regs[arg1] = getVal(arg2, regs)
    if ins == "add":
        arg1 = l[1]
        arg2 = l[2]
        if arg1 not in regs:
            regs[arg1] = 0
        regs[arg1] += getVal(arg2, regs)
    if ins == "mul":
        arg1 = l[1]
        arg2 = l[2]
        if arg1 not in regs:
            regs[arg1] = 0
        regs[arg1] *= getVal(arg2, regs)
    if ins == "mod":
        arg1 = l[1]
        arg2 = l[2]
        if arg1 not in regs:
            regs[arg1] = 0
        regs[arg1] = regs[arg1] % getVal(arg2, regs)
    if ins == "rcv":
        if getVal(l[1], regs) != 0 or True:
            if len(q2) > 0:
                regs[l[1]] = q2.pop(0)
                hold1 = False
            else:
                hold1 = True
    if ins == "jgz":
        arg1 = l[1]
        arg2 = l[2]
        if arg1 not in regs:
            regs[arg1] = 0
        if getVal(arg1, regs) > 0:
            i += getVal(arg2, regs) - 1
            
    if ins2 == "snd":
        q2.append(getVal(l2[1], regs2))
        counter += 1
    if ins2 == "set":
        arg1 = l2[1]
        arg2 = l2[2]
        if arg1 not in regs2:
            regs2[arg1] = 0
        regs2[arg1] = getVal(arg2, regs2)
    if ins2 == "add":
        arg1 = l2[1]
        arg2 = l2[2]
        if arg1 not in regs2:
            regs2[arg1] = 0
        regs2[arg1] += getVal(arg2, regs2)
    if ins2 == "mul":
        arg1 = l2[1]
        arg2 = l2[2]
        if arg1 not in regs2:
            regs2[arg1] = 0
        regs2[arg1] *= getVal(arg2, regs2)
    if ins2 == "mod":
        arg1 = l2[1]
        arg2 = l2[2]
        if arg1 not in regs2:
            regs2[arg1] = 0
        regs2[arg1] = regs2[arg1] % getVal(arg2, regs2)
    if ins2 == "rcv":
        if getVal(l2[1], regs2) != 0 or True:
            if len(q1) > 0:
                regs2[l2[1]] = q1.pop(0)
                hold2 = False
            else:
                hold2 = True
    if ins2 == "jgz":
        arg1 = l2[1]
        arg2 = l2[2]
        if arg1 not in regs2:
            regs2[arg1] = 0
        if getVal(arg1, regs2) > 0:
            j += getVal(arg2, regs2) - 1

    if not hold1:
        i += 1
    if not hold2:
        j += 1

    if hold1 and hold2:
        if steppers == 1:
            print(counter)
            exit()
        else:
            steppers = 1
    else:
        steppers = 0
print(counter)
