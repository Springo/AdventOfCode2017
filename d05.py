def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line)
    return lines

lines = readFile("d05input.txt")
ints = []
for line in lines:
    splitline = line.split()
    ints.append(int(line))

iters = 0
max = len(ints)
done = False
pos = 0
val = 0
while not done:
    iters += 1
    val = ints[pos]
    if val >= 3:
        ints[pos] -= 1
    else:
        ints[pos] += 1
    pos += val
    if pos < 0 or pos >= max:
        done = True
print(iters)
