def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines

lines = readFile("d01dat.txt")
line = lines[0]
checker = line + line
dist = len(line) // 2
sum = 0
for i in range(len(line)):
    a = int(line[i])
    b = int(checker[i + dist])
    if a == b:
        sum += a

print(sum)