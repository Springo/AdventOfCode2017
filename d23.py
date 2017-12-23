def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


lines = readFile("d23input.txt")
strlines = []
for line in lines:
    splitline = line.split()
    strlines.append(splitline)

regs = dict()
regs['a'] = 1

def getVal(n, dic):
    if ord(n[0]) < 58:
        return int(n)
    else:
        if n not in dic:
            dic[n] = 0
        return dic[n]

counter = 0

i = 0
while i < len(strlines):
    l = strlines[i]
    ins = l[0]
    if ins == "set":
        arg1 = l[1]
        arg2 = l[2]
        if arg1 not in regs:
            regs[arg1] = 0
        regs[arg1] = getVal(arg2, regs)
    if ins == "sub":
        arg1 = l[1]
        arg2 = l[2]
        if arg1 not in regs:
            regs[arg1] = 0
        regs[arg1] -= getVal(arg2, regs)
    if ins == "mul":
        arg1 = l[1]
        arg2 = l[2]
        if arg1 not in regs:
            regs[arg1] = 0
        regs[arg1] *= getVal(arg2, regs)
        counter += 1
    if ins == "jnz":
        arg1 = l[1]
        arg2 = l[2]
        if arg1 not in regs:
            regs[arg1] = 0
        if getVal(arg1, regs) != 0:
            i += getVal(arg2, regs) - 1

    i += 1
print(regs['h'])
