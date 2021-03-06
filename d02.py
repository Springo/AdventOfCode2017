def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines

lines = readFile("d02input.txt")
intlines = []
for line in lines:
    splitline = line.split()
    intlines.append([int(val) for val in splitline])
checksum = 0
for line in intlines:
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            if line[i] % line[j] == 0:
                checksum += line[i] // line[j]
            if line[j] % line[i] == 0:
                checksum += line[j] // line[i]
    #checksum += max(line) - min(line)

print(checksum)